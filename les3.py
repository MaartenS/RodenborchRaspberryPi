from gpiozero import LED
from pyquery import PyQuery as pq

d = pq(url='https://www.nu.nl/weer')
temp = int(d('div.molecule-weatherheader-current > span.temperature > h1')[0].text.split(' ')[0])

led = LED(17)

if temp >= 0:
    led.off()
    print('dooi')
else:
    led.on()
    print('het vriest')

led.close()