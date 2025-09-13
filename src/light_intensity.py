from machine import ADC, Pin
import time

sensor = ADC(Pin(26))
while True:
    print(sensor.read_u16())
    time.sleep(0.2)
