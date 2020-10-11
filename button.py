import RPi.GPIO as GPIO

btnGpio = 23 # ボタンにつながったGPIOの番号を変数に入れる

GPIO.setmode(GPIO.BCM)
GPIO.setup(btnGpio, GPIO.IN) # 変数btnGpioの値のGPIOピンを入力モードに設定する

print(GPIO.input(btnGpio)) # 現在のボタンの入力状態をShellビューに表示する

GPIO.cleanup()
