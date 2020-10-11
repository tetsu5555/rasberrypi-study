import RPi.GPIO as GPIO
import dht11

tempGpio = 4

GPIO.setmode(GPIO.BCM)
dht.stat = dht11.DHT11(pin = tempGpio) # DHT11の２番ピンにつながったGPIOピン番号を指定する

stat = dhtStat.read() # 変数statにDHT11で読み取ったセンサーの情報を入力する
print(stat.temperature) # 変数statに格納されているtemperatureの情報を画面に表示する

GPIO.cleanup()
