import RPi.GPIO as GPIO
import time

motorGpio = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(motorGpio, GPIO.OUT)

GPIO.output(motorGpio, True)
time.sleep(1)
GPIO.output(motorGpio, False)

GPIO.cleanup() // 使っていたすべてのGPIOの信号をすべて止める
