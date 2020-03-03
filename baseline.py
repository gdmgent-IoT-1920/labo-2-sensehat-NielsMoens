from sense_hat import SenseHat
from random import randint

sense = SenseHat()
sense.set_rotation(180)

def randomC():
    return randint(0,255)

def main():
    while True:
        sense.show_message("Hello! We are New Media Development:)", text_colour=[randomC(),randomC(),randomC()],back_colour=[randomC(),randomC(),randomC()])

try:
    main()
except (KeyboardInterrupt, SystemExit):
    print('Programma sluiten')
finally:
    print('Opkuisen v/d matrix')
    sense.clear()
    sys.exit(0)