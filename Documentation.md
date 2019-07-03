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