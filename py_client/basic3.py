import requests
#django model instance as an API response
endpoint = "http://127.0.0.1:8000/api/models/"

get_response = requests.get(endpoint)
print("text >", get_response.text)
print("json >", get_response.json())
print("status", get_response.status_code)
