from gpiozero import Button
from picamera import PiCamera
import RPi.GPIO as IO
import time
from signal import pause
import os
from Naked.toolshed.shell import execute_js, muterun_js

IO.setwarnings(False)       #do not show any warnings
IO.setmode (IO.BCM)         #we are programming the GPIO by BCM pin numbers. (PIN39 as 'GPIO19')
IO.setup(19,IO.OUT)         # initialize GPIO19 as an output.
IO.setup(26,IO.IN)               #initialize GPIO26 as input
button = Button(26)

camera = PiCamera()

origin = '/home/pi/Desktop/project/pictures/origin.jpg'

def take_picture(pic):
    #camera.start_preview()
    #time.sleep(3)
    camera.capture(pic)
    #camera.stop_preview()

while 1:
    diff = 0
    button.wait_for_press()
    start_time = time.time()
    
    while button.is_active:
        now_time = time.time()
        diff = -start_time+now_time

    if diff >= 5 :           #long hold
        IO.output(19, True)
        camera.capture(origin)
        os.system("gpicview " + origin)
        IO.output(19,False)
        
    else:                   #short hold
        for i in range(3):
            sleep(7);
            take_picture('/home/pi/Desktop/project/pictures/'+ str(i) + '.jpg')
        response = muterun_js('mismatch.js')
        if response.exitcode == 0:
            print(response.stdout)
