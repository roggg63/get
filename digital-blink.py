import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

number = 26
state = 0
period = 1.0

GPIO.setup(number, GPIO.OUT)

while Tru:
    GPIO.output(number, state)
    state = not state
    time.sleep(period)
