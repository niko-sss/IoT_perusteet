from machine import Pin
import time

# Set up PIR sensor and onboard LED
pir = Pin(18, Pin.IN)
led = Pin("LED", Pin.OUT)

while True:
    if pir.value() == 1:
        led.value(1)
        print("Motion detected")
    else:
        led.value(0)
    time.sleep(0.2)