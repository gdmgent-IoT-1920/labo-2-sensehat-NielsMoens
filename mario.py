from sense_hat import SenseHat

sense =SenseHat()
sense.set_rotation(0)

r=(255,0,0)
bl=(0,0,255)
br=(146,55,2)
p=(248,198,165)
bk=(11,15,14)
o=(0,0,0)


while True:
    mario = [
        o, o, r, r, r, r, o, o,
        o, br, br, p, bk, p, p, o,
        br, p, br, br, p, bk, p, p,
        o, br, br, p, p, p, o, o,
        o, o, r, bl, r, bl, r, o,
        o, r, r, bl, bl, bl, r, r,
        o, p, bk, r, bl, r, bk, p,
        o, o, br, br, bk, br, br, o
    ]
    sense.set_pixels(mario)
try:
    main()
except (KeyboardInterrupt, SystemExit):
    print('Programma sluiten')
finally:
    print('Opkuisen v/d matrix')
    sense.clear()
    sys.exit(0)
