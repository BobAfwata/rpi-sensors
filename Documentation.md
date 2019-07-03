Software
========
Install postman for testing the api

Download the postman client

Install requests using pip

pip install requests 
Software Design
==============
The programme uses requests to post and get sensor data from the web api
The request library 

import requests

url = "..........."
r = requests.post(url,params)


Reading sensor value 
===================
Before reading sensor value the Trig and echo pins needs to be pulled high with delays as shown 

GPIO.setup(trig_pin,GPIO.OUT)

The sensor values are sampled over time into a variable called distance

a timing function is used for measuring the interval between the measurements
timing is required to cause a delay and help in proper reading of the sensor values
Timing the measurments
=====================
pulse_end = time.time()                 #Time of the last HIGH pulse 


Create a variable containing the device id and distance to be used as parameters for the http request

payload = {'sensor_id': '044ea4f4-fd82-482c-97d1-7c190c70cbd7', 'value': distance}

Finally  the payload variable is sent via a http requests

r = requests.post(url, data=payload)




Hardware
========
read sensor data 
Ultrasonic sensor uses 4 pins
Ground 
Power - Vcc
Trigger 
Echo

connect the sensor to the pi using the various sets of echo and trig pins
ie sensor 1 in pins 23 and 24

ssh into the raspberry pi 

sudo ssh pi@pi_ipadress

run the main python file

python main.py

Results 
=======
THe serial displays the sensor values
The sensor data is sent to the api 