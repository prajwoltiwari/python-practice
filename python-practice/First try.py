import requests
import json

base_url = "https://reqres.in"
response = requests.get(base_url + "/api/users?page=2")
print(json.dumps(response.json(), indent=4))