import requests
import json 
#sensor_url = http://ultrapisensor.caramacs.com/api/sensor_data

data_from_pi = {'DeviceId':1234, 'distance1': 100 } #, 'distance2': 150, 'distance3':123, 'distance4':112, 'distance':129}

print('Sending sensor data ........')

response = requests.post('http://ultrapisensor.caramacs.com/api/sensor_data', json=data_from_pi)

if response.ok:
    print(response.json()) #--> {'temp_1': 100, 'temp_2': 150}


print('Getting sensor data ........')
get_response = requests.get('http://ultrapisensor.caramacs.com/api/sensor_data', json=data_from_pi)
if get_response.ok:
    print(get_response.json())
    #print(get_response.json()) #--> {'temp_1': 100, 'temp_2': 150}

