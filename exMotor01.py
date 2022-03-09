#+NPN S8050
import RPi.GPIO as GPIO
import time

MT1=17

#GPIO.setmode(GPIO.BOARD)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(MT1,GPIO.OUT)

print("Start Motor")
GPIO.output(MT1,GPIO.HIGH)
time.sleep(2)
GPIO.output(MT1,GPIO.LOW)
print("Stop Motor")
