import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

L1=16
L2=20
L3=21
L4=5

C1=6
C2=13
C3=19
C4=26

GPIO.setup(L1, GPIO.OUT)
GPIO.setup(L2, GPIO.OUT)
GPIO.setup(L3, GPIO.OUT)
GPIO.setup(L4, GPIO.OUT)

GPIO.setup(C1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def readLine(line,characters):
    GPIO.output(line, GPIO.HIGH)
    txt=''
    if(GPIO.input(C1)==1):
       #print(characters[0])
       txt = characters[0]
       if txt =='1':
            print('Number : 1')
       elif txt=='4':
            print('Number : 4 Hello')
       else:
            print('Number : 7,*')
    if(GPIO.input(C2)==1):
       #print(characters[1])
       txt = characters[0]
       if txt =='1':
            print('Number : 2')
       elif txt=='4':
            print('Number : 5 Hello')
       else:
            print('Number : 8,0')
    if(GPIO.input(C3)==1):
       #print(characters[2])
       txt = characters[0]
    if(GPIO.input(C4)==1):
       #print(characters[3])
       txt = characters[0]
    GPIO.output(line, GPIO.LOW)
try:
    while True:
       readLine(L1,["1","2","3","A"])#readLine(L1,["A","3","2","1"])
       readLine(L2,["4","5","6","B"])
       readLine(L3,["7","8","9","C"])
       readLine(L4,["*","0","#","D"])
       time.sleep(0.2)
except KeyboardInterrupt:
    print("\n!!! Application Stop !!!")