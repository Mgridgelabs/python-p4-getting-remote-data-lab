import requests
import json

class GetRequester:
    # Initialize the class with a URL
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        # Send a GET request to the URL and return the body of the response 
        response = requests.get(self.url)  
        return response.content  # Returns raw response content

    # Convert the response content to JSON format and return the Python object
    def load_json(self):
        # Use get_response_body to fetch data, then return it as a Python object
        response_body = self.get_response_body()  
        return json.loads(response_body)  # Parse the JSON response

# Create an instance of GetRequester
get_requester = GetRequester('https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json')

# Load the JSON data from the URL
data = get_requester.load_json()
print(data)

