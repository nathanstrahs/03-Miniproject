from machine import Pin, PWM, ADC
import time

# Buzzer on GP0
buzzer = PWM(Pin(0))
buzzer.duty_u16(32768)   # 50% duty

# Light sensor on GP26 (ADC0)
sensor = ADC(Pin(26))

# Tune this threshold to your environment
THRESHOLD = 12000

while True:
    value = sensor.read_u16()
    print("Light sensor:", value)

    if value > THRESHOLD:
        buzzer.freq(523)   # Bright → High C (523 Hz)
        print("Bright → High note")
    else:
        buzzer.freq(262)   # Dark → Low C (262 Hz)
        print("Dark → Low note")

    time.sleep(0.2)
