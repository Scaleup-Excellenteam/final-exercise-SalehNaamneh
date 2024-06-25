# Presentation Summarizer

This project provides a script to process PowerPoint presentations and generate succinct explanations for each slide using the OpenAI GPT-3.5 model.

## Table of Contents
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)
- [File Descriptions](#file-descriptions)
- [License](#license)

## Requirements
- Python 3.7 or higher
- An OpenAI API key

## Installation
1. **Clone the Repository**
    ```sh
    git clone https://github.com/yourusername/PresentationSummarizer.git
    cd PresentationSummarizer
    ```

2. **Set Up a Virtual Environment**
    ```sh
    python -m venv .venv
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
    ```

3. **Install Dependencies**
    ```sh
    pip install -r requirements.txt
    ```

4. **Set Up the OpenAI API Key**
    - Create a `.env` file in the project root and add your OpenAI API key:
      ```
      OPENAI_API_KEY=your_openai_api_key
      ```

## Usage
1. **Place Your Presentation**
    - Ensure your PowerPoint presentation file is in the project directory. The default file name is `logging_debugging_getting_into_a_large_codebase.pptx`. Adjust the file name in the `main.py` if necessary.

2. **Run the Script**
    ```sh
    python main.py
    ```

3. **Output**
    - The script will generate a JSON file with the same name as the presentation file, containing explanations for each slide.

## Testing
1. **Install Testing Dependencies**
    ```sh
    pip install pytest
    ```

2. **Run Tests**
    ```sh
    pytest test/GptTest.py
    ```

    - Ensure the demo presentation file `logging_debugging_getting_into_a_large_codebase.pptx` is present in the project directory.
    - The test script `test/GptTest.py` runs the main script and checks if the output JSON file is created.

## File Descriptions
- `main.py`: Main script to process the PowerPoint presentation and generate explanations.
- `requirements.txt`: Lists the dependencies needed for the project.
- `test/GptTest.py`: Contains the test to verify the script's functionality.
- `logging_debugging_getting_into_a_large_codebase.pptx`: Example PowerPoint presentation used for testing (should be included in the repository or replaced with your own file).

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

