from machine import Pin
import time
import machine

led = Pin(16, Pin.OUT)

while True:
    led.value(1)
    time.sleep(1)
    led.value(0)
    time.sleep(1)