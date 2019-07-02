import requests

payload = {'sensor_id': 'ead37d60-9cf4-11e9-a2a3-2a2ae2dbcce4', 'value': '500'}

r = requests.post("http://ultrapisensor.caramacs.com/api/sensor_data", data=payload)

print(r.status_code)