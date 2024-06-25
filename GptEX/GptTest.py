import os
import pytest
from subprocess import run, PIPE

# Define paths
SCRIPT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'main.py'))
DEMO_PRESENTATION_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'logging_debugging_getting_into_a_large_codebase.pptx'))

def test_script_runs_and_output_file_exists():
    # Run the script with the demo presentation using subprocess
    result = run(['python', SCRIPT_PATH], stdout=PIPE, stderr=PIPE, text=True)

    # Assert that the script ran successfully (exit code 0)
    assert result.returncode == 0, f"Script failed with output: {result.stdout} and errors: {result.stderr}"

    # Check that the output JSON file exists
    output_file = os.path.splitext(DEMO_PRESENTATION_PATH)[0] + '.json'
    assert os.path.exists(output_file)

