from flask import Flask, request, jsonify, render_template, url_for
from flask_wtf import FlaskForm
from wtforms import FileField
from wtforms.fields.simple import SubmitField
from werkzeug.utils import secure_filename
from datetime import datetime
import uuid
import threading
import pathlib
import logging
import os

from explainer.GptExplainer import MainFunc

app = Flask(__name__, template_folder='../templates')
app.config['SECRET_KEY'] = '123'
app.config['UPLOAD_FOLDER'] = pathlib.Path(os.path.join(os.getcwd(), 'uploads'))
app.config['OUTPUT_FOLDER'] = pathlib.Path(os.path.join(os.getcwd(), 'outputs'))

# Function to generate unique filename
def generate_unique_filename(file_name: str, file_ext: str) -> str:
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    random_uid = uuid.uuid4()
    return f"{file_name}_{current_time}_{random_uid}{file_ext}"

class UploadFileForm(FlaskForm):
    file = FileField('File')
    submit = SubmitField("Upload File")

def background_task(filepath):
    status = MainFunc(filepath)
    if status == 1:
        print(f"Task completed successfully: {filepath}")
    else:
        print("Failed to generate explanation")

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    form = UploadFileForm()
    if request.method == 'POST' and form.validate_on_submit():
        file = form.file.data
        filename = secure_filename(file.filename)
        logging.debug(f"Received file: {filename}")

        if not filename.endswith(".pptx"):
            return jsonify({"error": "This file is not supported. Only PPTX files are supported."}), 400

        unique_filename = generate_unique_filename(*os.path.splitext(filename))
        upload_path = app.config['UPLOAD_FOLDER'] / unique_filename
        file.save(upload_path)
        threading.Thread(target=background_task, args=(upload_path,)).start()

        return jsonify({"uid": unique_filename.split('_')[-1]})

    return render_template('index.html', form=form)

@app.route('/status', methods=['GET'])
def check_status():
    uid = request.args.get('uid')
    if not uid:
        return render_template('status_result.html', error="No UID provided")

    for file in app.config['UPLOAD_FOLDER'].iterdir():
        if uid in file.name:
            original_filename = "_".join(file.name.split("_")[:-2])
            timestamp = file.name.split("_")[-2]
            output_file = app.config['OUTPUT_FOLDER'] / f"{file.stem}.json"

            if output_file.exists():
                with open(output_file) as f:
                    explanation = f.read()
                return render_template('status_result.html', status="done", filename=original_filename, timestamp=timestamp, explanation=explanation)
            else:
                return render_template('status_result.html', status="pending", filename=original_filename, timestamp=timestamp)

    return render_template('status_result.html', error="File not found")

if __name__ == '__main__':
    app.config['UPLOAD_FOLDER'].mkdir(exist_ok=True)
    app.config['OUTPUT_FOLDER'].mkdir(exist_ok=True)
    app.run(port=5000)

