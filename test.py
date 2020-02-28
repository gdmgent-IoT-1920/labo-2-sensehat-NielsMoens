from sense_hat import SenseHat
import sys

sense = SenseHat()
sense.set_imu_config(False, False, False)

def main():
  while True: 
    sense.set_pixel(0,0,0,255,0)
    sense.set_pixel(1,1,255,0,0)
    sense.set_pixel(2,2,0,0,255)
    sense.set_pixel(3,3,255,255,0)
    sense.set_pixel(4,4,0,255,255)
    sense.set_pixel(5,5,100,10,50)
    sense.set_pixel(6,6,80,100,50)
    sense.set_pixel(7,7,0,255,0)
    
try:
	main()
except (KeyboardInterrupt, SystemExit):
	print('Programma sluiten')
finally:
	print('Opkuisen v/d matrix')
	sense.clear()
	sys.exit(0)
