import requests
#echoing get
#getting data from the database
endpoint = "http://127.0.0.1:8000/api/"
get_response = requests.post(endpoint, params={"abc":123}, json = {"query": "Hello django from this end of basic2.py"})

print(get_response.json())
