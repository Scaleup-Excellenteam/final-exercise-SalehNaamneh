import requests
import json

class GPTExplainerClient:
    def __init__(self, base_url):
        """
        Initialize the client with the base URL of the web API.
        """
        self.base_url = base_url

    def upload(self, file_path):
        """
        Upload a file to the server.

        Args:
            file_path (str): Path to the file to be uploaded.

        Returns:
            str: The UID of the uploaded file.

        Raises:
            HTTPError: If the server returns an error response.
        """
        with open(file_path, 'rb') as f:
            files = {'file': f}
            response = requests.post(f"{self.base_url}/upload", files=files)
            if response.status_code == 200:
                return response.json()['uid']
            else:
                response.raise_for_status()

    def status(self, uid):
        """
        Check the status of a file processing.

        Args:
            uid (str): The UID of the file.

        Returns:
            dict: The status of the file processing.

        Raises:
            HTTPError: If the server returns an error response.
        """
        response = requests.get(f"{self.base_url}/status", params={'uid': uid})
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

class Status:
    def __init__(self, status, filename, timestamp, explanation):
        """
        Initialize the status object.

        Args:
            status (str): The status of the file processing.
            filename (str): The original filename.
            timestamp (str): The timestamp of the upload.
            explanation (str): The explanation generated for the file.
        """
        self.status = status
        self.filename = filename
        self.timestamp = timestamp
        self.explanation = explanation

    def is_done(self):
        """
        Check if the file processing is done.

        Returns:
            bool: True if the processing is done, False otherwise.
        """
        return self.status == 'done'

    @classmethod
    def from_json(cls, json_data):
        """
        Create a Status object from JSON data.

        Args:
            json_data (dict): The JSON data containing status information.

        Returns:
            Status: The Status object created from JSON data.
        """
        return cls(
            status=json_data['status'],
            filename=json_data['filename'],
            timestamp=json_data['timestamp'],
            explanation=json_data['explanation']
        )
