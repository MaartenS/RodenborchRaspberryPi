#!/usr/bin/python
import time
import cv2
import requests
from gpiozero import LED, LightSensor, DigitalInputDevice

led = LED(17)
sensor = DigitalInputDevice(4)

sensor.when_activated = led.on
sensor.when_deactivated = led.off

while True:
    time.sleep(1)
