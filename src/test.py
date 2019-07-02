import requests


#url = 'https://api.exchangeratesapi.io/latest'
url = 'http://ultrapisensor.caramacs.com/api/sensor_data'
r = requests.get(url)
print(r.text)


r = requests.post('http://ultrapisensor.caramacs.com/api/sensors', data = {'name':'raspberry', 'device_uid':'123e4567-e89b-12d3-a456-426655440000'})

print(r.status_code)
print(r.text)

#send sensor data 
payload = {'value': 100, 'sensor_uid': 200}

sensor_data = requests.get('http://ultrapisensor.caramacs.com/api/sensor_data', data={'value': '100', 'sensor_uid': 'u-200'})
print(sensor_data.text)

#add devices

r = requests.get('http://ultrapisensor.caramacs.com/api/devices', data={'name': 'device1', 'user_id': 'u-200'})
print(r.text)

