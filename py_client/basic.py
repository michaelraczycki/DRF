import requests
import json

endpoint = "http://localhost:8000/api/"

get_response = requests.get(endpoint,params={'abc': 123} ,json={"content": "Some cool content."})
print(get_response.status_code)
print(get_response.json())