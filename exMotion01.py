import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(23, GPIO.IN)
GPIO.setup(24, GPIO.OUT)

i = 0
try:
    time.sleep(2)
    while True:
        i += 1
        if GPIO.input(23):
            GPIO.output(24,True)
            time.sleep(0.5)
            GPIO.output(24,False)
            print("Motion Detected...."+str(i))
            time.sleep(0.5)
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup(24)
    GPIO.cleanup()
