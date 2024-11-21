import requests
#creating your first API View
endpoint = "http://127.0.0.1:8000/api"

get_response = requests.get(endpoint)

print("text", get_response.text)
print("json", get_response.json())
print("status", get_response.status_code)
