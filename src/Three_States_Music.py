from machine import Pin, PWM, ADC
import time

# Buzzer on GP0
buzzer = PWM(Pin(0))
buzzer.duty_u16(32768)   # 50% duty

# Light sensor on GP26 (ADC0)
sensor = ADC(Pin(26))

# You define these thresholds
LOW_THRESHOLD = 20000    # example value, set yourself
HIGH_THRESHOLD = 40000   # example value, set yourself

while True:
    value = sensor.read_u16()
    print("Light sensor:", value)

    if value < LOW_THRESHOLD:
        buzzer.freq(262)   # Dark → Low C (262 Hz)
        print("Dark → Low note")
    elif value < HIGH_THRESHOLD:
        buzzer.freq(392)   # Medium → G (392 Hz)
        print("Medium → Mid note")
    else:
        buzzer.freq(523)   # Bright → High C (523 Hz)
        print("Bright → High note")

    time.sleep(0.2)
