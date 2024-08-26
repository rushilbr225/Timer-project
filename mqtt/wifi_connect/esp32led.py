from machine import Pin
from time import sleep

led = Pin(2, Pin.OUT) # blink Pin number 2

def blink():
    print("Starting the blink for 10 times")
    for _ in range(10):
        led.value(1)
        sleep(1)
        led.value(0)
        sleep(1)
    print("Ending the blink for 10 times")
#blink()

def onOrOff(value):
    led.value(value)

#onOrOff(1)
onOrOff(0)