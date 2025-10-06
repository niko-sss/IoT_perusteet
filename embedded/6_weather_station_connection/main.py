import time
import network
import urequests
import dht
from machine import Pin

time.sleep(0.1)

ssid = 'Wokwi-GUEST'
password = ''

THINGSPEAK_API_KEY= ''
THINGSPEAK_URL = 'https://api.thingspeak.com/update'

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

print("Connecting to Wi-Fi...", end="")
while not wlan.isconnected():
    print(".", end="")
    time.sleep(0.5)

print("\nConnected!")
print("IP address:", wlan.ifconfig()[0])

sensor = dht.DHT22(Pin(15))

def send_to_thingspeak(temp):
    if temp is None:
        return
    try:
        response = urequests.post(
            THINGSPEAK_URL,
            data='api_key={}&field1={}'.format(THINGSPEAK_API_KEY, temp),
            headers={'Content-Type': 'application/x-www-form-urlencoded'}
        )
        response.close()
    except Exception as e:
        print("Failed sending data: ", e)

while True:
    try:
        sensor.measure()
        temperature = sensor.temperature()
        print("Temperature:", temperature, "°C")
        send_to_thingspeak(temperature)
    except Exception as e:
        print("Error reading sensor or sending data:", e)
    time.sleep(15)
