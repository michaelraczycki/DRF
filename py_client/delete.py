import requests

product_id = input("Enter product id: \n")
try:
    product_id = int(product_id)
except ValueError:
    print("Product id must be an integer")
    exit()

if product_id:
    endpoint = f"http://localhost:8000/api/products/{product_id}/delete"

get_response = requests.delete(endpoint)
print(get_response.status_code)
