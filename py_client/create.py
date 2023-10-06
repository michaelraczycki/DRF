import requests

endpoint = "http://localhost:8000/api/products/"

get_response = requests.post(endpoint, json={"title": "this field is done"})
print(get_response.json())
