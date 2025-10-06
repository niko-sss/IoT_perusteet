from machine import Pin
from utime import sleep

buzzer = Pin(10, Pin.OUT)
switch = Pin(11, Pin.IN, Pin.PULL_DOWN)
external_led1 = Pin(15, Pin.OUT)
external_led2 = Pin(14, Pin.OUT)
external_led3 = Pin(13, Pin.OUT)

while True:
    external_led3.value(False)
    external_led1.value(True)
    sleep(5)
    external_led1.value(False)
    external_led2.value(True)
    sleep(1)
    external_led2.value(False)
    external_led3.value(True)
    sleep(5)
    if switch.value():
        buzzer.value(True)
        sleep(5)
        buzzer.value(False)
