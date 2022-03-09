import RPi.GPIO as GPIO
GPIO.setwarnings(False)
#GPIO.setmode(GPIO.BOARD)
GPIO.setmode(GPIO.BCM)

MATRIX= [
            ["A","3","2","1"],
            ["B","6","5","4"],
            ["C","9","8","7"],
            ["D","#","0","*"]
        ]
ROW = [5, 6, 13, 19]
COL = [12, 16, 20, 21]

for j in range(4):
    GPIO.setup(COL[j], GPIO.OUT)
    GPIO.output(COL[j],1)

for i in range(4):
    GPIO.setup(ROW[i], GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    print("==> Start Input KeyPad <==")
    data = ""
    while( True ):
        ###PUT CODE HERE START###
        for j in range(4):
            GPIO.output(COL[j],0)
            for i in range(4):
                if GPIO.input(ROW[i]) == 0:
                    if MATRIX[i][j] == "#":
                        print("Data input = "+data)
                        data=""
                    else:
                        data = data + MATRIX[i][j]
                        print(MATRIX[i][j])
                    while(GPIO.input(ROW[i]) == 0):
                        pass
            GPIO.output(COL[j],1)
        ###PUT CODE HERE END###

except KeyboardInterrupt:
    print("==> End Input KeyPad <==")
    GPIO.cleanup()

