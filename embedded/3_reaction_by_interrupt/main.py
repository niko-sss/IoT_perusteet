import machine
from machine import Pin
from utime import sleep, ticks_ms, ticks_diff
import urandom

led = Pin(15, Pin.OUT)
switch = Pin(14, Pin.IN, Pin.PULL_DOWN)

reaction_time = 0
start_time = 0
pressed = False


def button_press(pin):
    global pressed, reaction_time
    if not pressed:
        reaction_time = ticks_diff(ticks_ms(), start_time)
        pressed = True

switch.irq(trigger=Pin.IRQ_RISING, handler=button_press)

while True:
    pressed = False
    
    print("Ready")
    led.value(False)
    sleep(2)

    print("Blink incoming in 2-6 seconds")
    sleep(urandom.randrange(2, 6))
    led.value(1)
    start_time = ticks_ms()

    while not pressed:
        pass

    led.value(0)
    print("Your reaction time was:", reaction_time, "ms")
    sleep(2)