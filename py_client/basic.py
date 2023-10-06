import json

import requests

endpoint = "http://localhost:8000/api/"

get_response = requests.post(endpoint, json={"title": "sometitle"})
print(get_response.status_code)
print(get_response.json())
