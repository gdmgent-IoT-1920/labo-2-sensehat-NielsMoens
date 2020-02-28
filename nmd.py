from sense_hat import SenseHat
from time import sleep
from random import randint

sense =SenseHat()
sense.set_rotation(0)

red =(randint(0,255),randint(0,255),randint(0,255))
blue=(randint(0,255),randint(0,255),randint(0,255))
green=(randint(0,255),randint(0,255),randint(0,255))

while True:
    sense.show_letter("N", red)
    sleep(1)
    sense.show_letter("M", blue)
    sleep(1)
    sense.show_letter("D", green)
    sleep(3)
try:
    main()
except (KeyboardInterrupt, SystemExit):
    print('Programma sluiten')
finally:
    print('Opkuisen v/d matrix')
    sense.clear()
    sys.exit(0)