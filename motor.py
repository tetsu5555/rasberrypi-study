import RPi.GPIO as GPIO
import time

motorGpio = [24, 25] # この変数を変えることでモーターを逆回転させる
directRot = 0 # 回転方向を指定するための変数
waitTime = 1

GPIO.setmode(GPIO.BCM)
for setBcm in motorGpio:
    GPIO.setup(setBcm, GPIO.OUT)

while True:
    GPIO.output(motorGpio[directRot], True)
    time.sleep(waitTime)
    GPIO.output(motorGpio[directRot], False)
    time.sleep(waitTime)

GPIO.cleanup() # 使っていたGPIOの信号をすべて止める
