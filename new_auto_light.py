import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

led = 26
state = 1
signal = 6

GPIO.setup(led, GPIO.OUT)
GPIO.setup(signal, GPIO.IN)

while True:
    if GPIO.input(signal):
        state = not state
        GPIO.output(led, state)

        GPIO.output(led, 0)
    else:
        GPIO.output(led, 1)