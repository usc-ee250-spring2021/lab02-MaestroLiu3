""" EE 250L Lab 02: GrovePi Sensors

List team members here.
Jeffrey Liu
Insert Github repository link here.
"""
https://github.com/usc-ee250-spring2021/lab02-MaestroLiu3/tree/lab02
"""python3 interpreters in Ubuntu (and other linux distros) will look in a 
default set of directories for modules when a program tries to `import` one. 
Examples of some default directories are (but not limited to):
  /usr/lib/python3.5
  /usr/local/lib/python3.5/dist-packages

The `sys` module, however, is a builtin that is written in and compiled in C for
performance. Because of this, you will not find this in the default directories.
"""
import sys
import time
import numpy
# By appending the folder of all the GrovePi libraries to the system path here,
# we are successfully `import grovepi`
sys.path.append('../../Software/Python/')
# This append is to support importing the LCD library.
sys.path.append('../../Software/Python/grove_rgb_lcd')

from grove_rgb_lcd import *
import grovepi
potentiometer = 0 # rotary angle sensor on analog 0
"""This if-statement checks if you are running this python file directly. That 
is, if you run `python3 grovepi_sensors.py` in terminal, this if-statement will 
be true"""
if __name__ == '__main__':
    PORT = 4    # D4

    while True:
        #So we do not poll the sensors too quickly which may introduce noise,
        #sleep for a reasonable time of 200ms between each iteration.
        time.sleep(0.2)
	# read the sensor value from pot
        sensor_value = grovepi.analogRead(potentiometer)
	ultra_value = grovepi.ultrasonicRead(PORT)
        #read distance value from ultrasonic
        #print(grovepi.ultrasonicRead(PORT))
	#print("sensor_value =%d" %(sensor_value))
        print(sensor_value)
        setRGB(0,255,0)
        setText_norefresh(str(sensor_value) + "cm           " + "\n"  + str(ultra_value) + "cm " )
        while(sensor_value >  ultra_value):
            setText_norefresh(str(sensor_value) + "cm OBJ PRES" + "\n"+ str(ultra_value) + "cm ")
            setRGB(255,0,0)
            sensor_value = grovepi.analogRead(potentiometer)
            ultra_value = grovepi.ultrasonicRead(PORT)
        #setText_norefresh(str(grovepi.ultrasonicRead(PORT)) + "cm ")



#<<<<<<< HEAD
#=======

#>>>>>>> 1048cbfe0955e88f95024ca430dc7f8d9bb255a0
