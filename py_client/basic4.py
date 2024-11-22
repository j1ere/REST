import requests
#django model instance to dictionary
endpoint = "http://127.0.0.1:8000/api/models_serialized/"

get_response = requests.post(endpoint, params = {"abc":123}, json={"client":"i am happy"})

#print("json >", get_response.json())
print(get_response.headers)
print(get_response.json())
