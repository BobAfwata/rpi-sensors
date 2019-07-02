import requests, json

url = 'http://ultrapisensor.caramacs.com/api/sensor_data'

payload = {"sensor_id": "044ea4f4-fd82-482c-97d1-7c190c70cbd7", 
           "value": 51}

header = {"Content-type": "application/json",
          "Accept": "application/json"} 

response_decoded_json = requests.post(url, data=payload, headers=header)
response_json = response_decoded_json.json()

print(response_json)