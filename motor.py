import RPi.GPIO as GPIO
import time

motorGpio = 25 # この変数を変えることでモーターを逆回転させる

GPIO.setmode(GPIO.BCM)
GPIO.setup(motorGpio, GPIO.OUT)

GPIO.output(motorGpio, True)
time.sleep(1)
GPIO.output(motorGpio, False)

GPIO.cleanup() # 使っていたGPIOの信号をすべて止める
