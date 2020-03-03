from sense_hat import SenseHat
from random import randint
from time import sleep
import sys

sense = SenseHat()

r = (randint(100,255), randint(100,255), randint(100,255))
o = (0, 0, 0)

rect2v2 = [
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o,
o,o,o,r,r,o,o,o,
o,o,o,r,r,o,o,o,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o,
]
rect4v4 = [
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o,
o,o,r,r,r,r,o,o,
o,o,r,o,o,r,o,o,
o,o,r,o,o,r,o,o,
o,o,r,r,r,r,o,o,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o,
]
rect8v8 = [
o,o,o,o,o,o,o,o,
o,r,r,r,r,r,r,o,
o,r,o,o,o,o,r,o,
o,r,o,o,o,o,r,o,
o,r,o,o,o,o,r,o,
o,r,o,o,o,o,r,o,
o,r,r,r,r,r,r,o,
o,o,o,o,o,o,o,o,
]
rect16v16 = [
r,r,r,r,r,r,r,r,
r,o,o,o,o,o,o,r,
r,o,o,o,o,o,o,r,
r,o,o,o,o,o,o,r,
r,o,o,o,o,o,o,r,
r,o,o,o,o,o,o,r,
r,o,o,o,o,o,o,r,
r,r,r,r,r,r,r,r,
]

def main():
    while True:
        sense.set_pixels(rect2v2)
        sleep(0.1)
        sense.set_pixels(rect4v4)
        sleep(0.1)
        sense.set_pixels(rect8v8)
        sleep(0.1)
        sense.set_pixels(rect16v16)
        sleep(0.1)
        sense.set_pixels(rect8v8)
        sleep(0.1)
        sense.set_pixels(rect4v4)
        sleep(0.1)

try:
    main()
except (KeyboardInterrupt, SystemExit):
    print("programma sluiten")
finally:
    print("opkuisen van de matrix")
    sense.clear()
    sys.exit(0)