from machine import Pin, PWM, ADC
import time

# -----------------
# Buzzer on GP0
# -----------------
buzzer = PWM(Pin(0))
buzzer.duty_u16(32768)   # 50% duty (volume)

# -----------------
# RGB LED (common anode) on GP10, GP11, GP12
# -----------------
red = Pin(10, Pin.OUT)
green = Pin(12, Pin.OUT)
blue = Pin(11, Pin.OUT)

def set_color(r, g, b):
    """
    For common anode LED:
      1 = OFF, 0 = ON
    r, g, b are booleans (True/False or 1/0)
    """
    red.value(0 if r else 1)
    green.value(0 if g else 1)
    blue.value(0 if b else 1)

# -----------------
# Light sensor on GP26 (ADC0)
# -----------------
sensor = ADC(Pin(26))

# Adjust thresholds for your environment
LOW_THRESHOLD = 20000
HIGH_THRESHOLD = 40000

while True:
    value = sensor.read_u16()
    print("Light sensor:", value)

    if value < LOW_THRESHOLD:
        buzzer.freq(262)   # Dark → Low C
        set_color(1, 0, 0)  # Red
        print("Dark → Low note + Red")
    elif value < HIGH_THRESHOLD:
        buzzer.freq(392)   # Medium → G
        set_color(0, 1, 0)  # Green
        print("Medium → Mid note + Green")
    else:
        buzzer.freq(523)   # Bright → High C
        set_color(0, 0, 1)  # Blue
        print("Bright → High note + Blue")

    time.sleep(0.2)
