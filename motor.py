import RPi.GPIO as GPIO
import time

motorGpio = 25 # この変数を変えることでモーターを逆回転させる
waitTime = 1

GPIO.setmode(GPIO.BCM)
GPIO.setup(motorGpio, GPIO.OUT)

while True:
    GPIO.output(motorGpio, True)
    time.sleep(waitTime)
    GPIO.output(motorGpio, False)
    time.sleep(waitTime)

GPIO.cleanup() # 使っていたGPIOの信号をすべて止める
