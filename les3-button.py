import time
from gpiozero import LED, Button

led = LED(17)
button = Button(3)


def pressed():
    led.on()


def released():
    led.off()


button.when_pressed = pressed
button.when_released = released

while True:
    time.sleep(1)
