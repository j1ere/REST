import requests
#rest framework view and response
endpoint = "http://127.0.0.1:8000/api/drf_response/"

get_response = requests.post(endpoint, params={"abc":123}, json={"name":"jeremiah wambua"})

print(get_response.json())