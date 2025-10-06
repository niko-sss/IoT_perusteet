from machine import Pin

switch = Pin(14, Pin.IN, Pin.PULL_DOWN)
external_led = Pin(15, Pin.OUT)

while True:
    if switch.value():
        external_led.value(True)
    else:
        external_led.value(False)
