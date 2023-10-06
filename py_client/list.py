from getpass import getpass

import requests

endpoint = "http://localhost:8000/api/products/"
password = getpass()

auth_response = requests.post(
    "http://localhost:8000/api/auth/",
    data={"username": "cfe", "password": password},
)
print(auth_response.json())

if auth_response.status_code != 200:
    raise Exception("Could not authenticate user")
else:
    token = auth_response.json()["token"]
    headers = {"Authorization": f"Bearer {token}"}
    get_response = requests.get(endpoint, headers=headers)
    print(get_response.json())
