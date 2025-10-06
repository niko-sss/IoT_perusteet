from machine import Pin
from utime import sleep

external_led = Pin(15, Pin.OUT)

while True:
    external_led.toggle()
    sleep(1)
