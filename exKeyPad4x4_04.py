import RPi.GPIO as GPIO
GPIO.setwarnings(False)
from pad4pi import rpi_gpio
import time


# Setup Keypad
KEYPAD = [
        ["A","3","2","1"],
        ["B","6","5","4"],
        ["C","9","8","7"],
        ["D","#","0","*"]
]

# same as calling: factory.create_4_by_4_keypad, still we put here fyi:
ROW_PINS = [5, 6, 13, 19] # BCM numbering
COL_PINS = [12, 16, 20, 21] # BCM numbering
factory = rpi_gpio.KeypadFactory()

# Try keypad = factory.create_4_by_3_keypad() or 
# Try keypad = factory.create_4_by_4_keypad() #for reasonable defaults
# or define your own:
keypad = factory.create_keypad(keypad=KEYPAD, row_pins=ROW_PINS, col_pins=COL_PINS)


class KeyStore:
    def __init__(self):
        #list to store them
        self.pressed_keys =''

    #function to clear string
    def clear_keys(self):
        self.pressed_keys = self.pressed_keys.replace(self.pressed_keys,'')

    def store_key(self,key):
        if key=='#':
            #printing the sequence of keys.
            print(self.pressed_keys)
            self.clear_keys()
        else:
            self.pressed_keys += key

keys = KeyStore()

# store_key will be called each time a keypad button is pressed
keypad.registerKeyPressHandler(keys.store_key)


try:
    while(True):
        time.sleep(0.2)
except:
    keypad.cleanup()