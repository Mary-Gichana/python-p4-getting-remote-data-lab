import requests
import json

class GetRequester:
    def __init__(self, url):
        """
        Initializes the GetRequester with the provided URL.
        """
        self.url = url

    def get_response_body(self):
        """
        Sends a GET request to the URL and returns the raw response body as bytes.
        """
        response = requests.get(self.url)
        response.raise_for_status()  
        return response.content  

    def load_json(self):
        """
        Uses get_response_body to send a GET request and parse the JSON response.
        Returns a Python list or dictionary.
        """
        response_body = self.get_response_body()
        return json.loads(response_body)  
