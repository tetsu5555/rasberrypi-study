import RPi.GPIO as GPIO

motorGpio = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(motorGpio, GPIO.OUT)

GPIO.output(motorGpio, True)
