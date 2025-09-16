from machine import Pin
import time

# LED to make sure pico is running script
led = Pin("LED", Pin.OUT)
led.on()

# Send 3.3V to common anode (+)
led_vcc = Pin(11, Pin.OUT)
led_vcc.value(1)


# Setup pins as outputs
red = Pin(10, Pin.OUT)
green = Pin(12, Pin.OUT)
blue = Pin(11, Pin.OUT)

def set_color(r, g, b):
    """
    r, g, b = 0 or 1
    For common cathode:
        1 = ON, 0 = OFF
    For common anode:
        0 = ON, 1 = OFF
    """
    red.value(r)
    green.value(g)
    blue.value(b)

while True:
    # Cycle some colors
    set_color(0, 1, 1)   # Red
    time.sleep(1)
    set_color(1, 0, 1)   # Green
    time.sleep(1)
    set_color(1, 1, 0)   # Blue
    time.sleep(1)
    set_color(0, 0, 1)   # Yellow
    time.sleep(1)
    set_color(0, 0, 0)   # White (for common cathode; off for common anode)
    time.sleep(1)
    set_color(1, 1, 1)   # All off (for common cathode; all on for common anode)

