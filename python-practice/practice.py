import requests
import json

base_url = "http://103.198.9.172:9092"
response = requests.post((base_url + "/api/authentication/login/"), data = {
  "phone": "9860832382",
  "password": "Gabbu@123",
  "type": "passenger",
  "country_code": "+977"
})
print(json.dumps(response.json(), indent=4))
print(response)