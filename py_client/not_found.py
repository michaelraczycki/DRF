import requests

endpoint = "http://localhost:8000/api/products/1436256573456748/"

get_response = requests.get(endpoint)
print(get_response.status_code)
print(get_response.json())
