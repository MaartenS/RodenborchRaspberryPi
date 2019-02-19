#!/usr/bin/python
import time
import cv2
from gpiozero import LED, Button

led = LED(17)
button = Button(4)


def pressed():
    led.on()
    cam = cv2.VideoCapture(0)
    s, im = cam.read()
    cv2.imwrite("test.jpg",im)


def released():
    led.off()


button.when_pressed = pressed
button.when_released = released

while True:
    time.sleep(1)
