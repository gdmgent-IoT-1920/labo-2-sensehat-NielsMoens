from sense_hat import SenseHat
from random import randint
import time
import sys

sense = SenseHat()
ledcter = 0
ledcter2 = 0

def randInt():
    return randint(1,255), randint(1,255), randint(1,255)

def main():
    while True:
        sense.set_pixel(ledcter, ledcter2, [randInt()])
        time.sleep(0.1)
        sense.clear()
        
        if ledcter == 7 and ledcter2 == 7:
            ledcter = 0
            ledcter2 = 0
        elif ledcter2 == 7:
            ledcter += 1
            ledcter2 = 0
        else:
            ledcter2 +=1
try:
    main()
except (KeyboardInterrupt, SystemExit):
    print("programma sluiten")
finally:
    print("opkuisen van de ledCounter")
    sense.clear()
    sys.exit(0)