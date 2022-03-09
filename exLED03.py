from gpiozero import LED
import time
import RPi.GPIO as GPIO

led1=LED(18)
led2=LED(17)
t=.1

try:
    while True:
        led2.off()
        led1.on()
        time.sleep(t)
        led1.off()
        led2.on()
        time.sleep(t)
        led2.off()
        time.sleep(t)
        led1.on()
        led2.on()
        time.sleep(t)
        led1.off()
        led2.off()
        time.sleep(t)
except KeyboardInterrupt:
    print("Keyboard Interrupt Program")
except:
    print("Other Interrupt Program")
finally:
    GPIO.cleanup()
 
