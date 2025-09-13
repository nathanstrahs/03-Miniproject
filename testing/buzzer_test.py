from machine import Pin, PWM
import time

# Set up PWM on GP0
buzzer = PWM(Pin(0))

# Frequency doesn’t change the pitch for active buzzer,
# but we still need to set it (use ~1 kHz as a safe value)
buzzer.freq(1000)

while True:    
    # 50% duty cycle (range is 0–65535)
    buzzer.duty_u16(32768)

    # Let it buzz for 2 seconds
    time.sleep(2)

    # Stop the buzzer
    buzzer.duty_u16(0)
    buzzer.deinit()
    
    time.sleep(2)
