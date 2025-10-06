from machine import Pin
from utime import sleep

led = Pin("LED", Pin.OUT)  # "LED" is an alias for the onboard LED in MicroPython

while True:
    led.toggle()
    sleep(1)
