
### Files Overview

- **api/app.py**: The main Flask application file that defines routes for the welcome page, file upload, and status check. It uses Flask-WTF for handling file upload forms and runs background tasks for processing files.

- **client/client.py**: A Python client that interacts with the web API to upload files and check their status. It includes methods for uploading files and retrieving status information.

- **explainer/GptExplainer.py**: The script responsible for processing PPTX files. It extracts text from slides, generates explanations using GPT-3.5, and saves the results in a JSON file.

- **static/welcome_image.jpg**: An image used on the welcome page.

- **templates/welcome.html**: The HTML template for the welcome page, which includes a welcome message, an image, and a form to check the status of an uploaded file using its UID.

- **templates/index.html**: The HTML template for the file upload page, which includes a form to upload PPTX files.

- **templates/upload_result.html**: The HTML template for displaying the result after a file is uploaded, showing the unique identifier (UID) of the uploaded file.

- **templates/status_result.html**: The HTML template for displaying the status of a file processing based on the provided UID.


