import time
import requests
from gpiozero import LED, Button

led = LED(17)
button = Button(4)


def pressed():
    led.on()
    requests.get('http://192.168.10.100:8080/count')


def released():
    led.off()


button.when_pressed = pressed
button.when_released = released

while True:
    time.sleep(1)
