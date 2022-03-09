from gpiozero import LED
import time
import RPi.GPIO as GPIO

led1=LED(18)
led2=LED(17)
t=.1

try:
    print("==> Ctrl+C to End Program <==")
    i = 0
    while True:
        led2.off()
        led1.on()
        time.sleep(t)
        led1.off()
        led2.on()
        time.sleep(t)
        led2.off()
        time.sleep(t)
        i=i+1
        print("Loop : ", i )
        if i == 10:
            break
except KeyboardInterrupt:
    print("==> End Program by ctrl+c <==")
 
except ZeroDivisionError: #division by zero

except NameError: #name not define

except TypeError: #Can't convert 'int' object to str implicitly

except :
    print("==> End Program other Interupt <==")


finally:
    GPIO.cleanup()
    
    