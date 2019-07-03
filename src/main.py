#!/usr/bin/python
#encoding:utf-8

import RPi.GPIO as GPIO                    #Import GPIO library
import time                                #Import time library
GPIO.setmode(GPIO.BCM)                     #Set GPIO pin numbering 
import requests

SENSOR1_TRIG = 23                                  #Associate pin 15 to TRIG
SENSOR1_ECHO = 24                                  #Associate pin 14 to Echo

SENSOR2_TRIG = 20                                 #Associate pin 15 to TRIG
SENSOR2_ECHO = 21                                  #Associate pin 14 to Echo

SENSOR3_TRIG = 12                                 #Associate pin 15 to TRIG
SENSOR3_ECHO = 16                                #Associate pin 14 to Echo

SENSOR4_TRIG = 7                                 #Associate pin 15 to TRIG
SENSOR4_ECHO = 8                                  #Associate pin 14 to Echo

SENSOR5_TRIG = 5                                  #Associate pin 15 to TRIG
SENSOR5_ECHO = 6                                  #Associate pin 14 to Echo

trig_pins = {SENSOR1_TRIG,SENSOR2_TRIG,SENSOR3_TRIG,SENSOR4_TRIG,SENSOR5_TRIG}
echo_pins = {SENSOR1_ECHO,SENSOR2_ECHO,SENSOR3_ECHO,SENSOR4_ECHO,SENSOR5_ECHO}
GPIO.setwarnings(False)

url = 'http://ultrapisensor.caramacs.com/api/sensor_data'

def get_data(url):
    r = requests.get(url)
    print(r.text)

distance = 0

payload = {'sensor_id': '044ea4f4-fd82-482c-97d1-7c190c70cbd7', 'value': distance}

def send_sensor_data(url,payload):
    r = requests.post(url, data=payload)

    print(r.status_code)
    #end of sending data


def init_sensors(trig_pins,echo_pins):
    #trig_pins = {SENSOR1_TRIG,SENSOR2_TRIG,SENSOR3_TRIG,SENSOR4_TRIG,SENSOR5_TRIG}
    #echo_pins = {SENSOR1_ECHO,SENSOR2_ECHO,SENSOR3_ECHO,SENSOR4_ECHO,SENSOR5_ECHO}
    #set pins as output and input

    for i in trig_pins:
        GPIO.setup(i,GPIO.OUT)
        time.sleep(0.5)
    for i in echo_pins:
        GPIO.setup(i,GPIO.IN)                   #Set pin as GPIO in
    
    print('sensors successfully initialized....')

init_sensors(trig_pins,echo_pins)

def pull_trig_low(trig_pins):
    for i in trig_pins:
            GPIO.output(i, False)                 #Set TRIG as LOW
            time.sleep(0.0002)  


def pull_trig_high(trig_pins):
    for i in trig_pins:
            GPIO.output(i, True)                 #Set TRIG as LOW
            time.sleep(0.0002)  



def pull_echo_low(echo_pins):
    for i in echo_pins:
            GPIO.output(i, False)                 #Set TRIG as LOW
            time.sleep(0.0002)  

def pull_echo_high(echo_pins):
    for i in echo_pins:
            GPIO.output(i, True)                 #Set TRIG as LOW
            time.sleep(0.0002)  

def get_gpio_status(echo_pins):
    for i in echo_pins:
        if GPIO.input(i)==0:
            return 0
        else :
            return 1


while True:
    time.sleep(1)
    pull_trig_low(trig_pins)
    #GPIO.output(SENSOR1_TRIG, False)                 #Set TRIG as LOW
    print("Waiting For Sensors To Settle")
    time.sleep(0.0002)  
                              #Delay of 2 seconds
    pull_trig_high(trig_pins)
    #GPIO.output(SENSOR1_TRIG, True)                  #Set TRIG as HIGH
    time.sleep(0.00001)                      #Delay of 0.00001 seconds
    pull_trig_low(trig_pins)
    #GPIO.output(SENSOR1_TRIG, False)                 #Set TRIG as LOW

    while get_gpio_status(echo_pins)==0:
        pulse_start = time.time()              #Time of the last  LOW pulse

    while get_gpio_status(echo_pins)==1:               #Check whether Echo is HIGH
        pulse_end = time.time()                 #Time of the last HIGH pulse 
        pulse_duration = pulse_end - pulse_start  #pulse duration to a variable
        distance = pulse_duration * 17150        #Calculate distance
        distance = round(distance, 2)            #Round to two decimal points
    if distance > 20 and distance < 400:     #Is distance within range
        print("Distance:",distance - 0.5,"cm" ) #Distance with calibration
        payload = {'sensor_id': '044ea4f4-fd82-482c-97d1-7c190c70cbd7', 'value': distance}
        r = requests.post(url, data=payload)
        print(r.text)
        time.sleep(0.0002) 

        # send it to api 
    else:
        print("Out Of Range")                  #display out of range











