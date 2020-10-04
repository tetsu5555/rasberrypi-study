import RPi.GPIO as GPIO
import time

LedGpio = 18
WaitTime = 1

GPIO.setmode(GPIO.BCM)
GPIO.setup(LedGpio, GPIO.OUT)
GPIO.setwarnings(False)

GPIO.output(LedGpio, True)
time.sleep(WaitTime)
GPIO.output(LedGpio, False)

GPIO.cleanup()