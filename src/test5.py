import requests

distance = 500

payload = {'sensor_id': '044ea4f4-fd82-482c-97d1-7c190c70cbd7', 'value': '500'}

r = requests.post("http://ultrapisensor.caramacs.com/api/sensor_data", data=payload)

print(r.text)


#sensor_data = { distance1 : 500 , distance2 : 250 , distance3:235, distance4:34, distance5: 45}

"""

def post_data(sensor_data):
    for i in sensor_data:
        payload = {'sensor_id': '044ea4f4-fd82-482c-97d1-7c190c70cbd7', 'value': i}
        r = requests.post("http://ultrapisensor.caramacs.com/api/sensor_data", data=payload)
        print(r.text)

"""

