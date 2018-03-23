from gpiozero import Button
from picamera import PiCamera
import RPi.GPIO as IO
import time
import socket
from signal import pause
import os
from Naked.toolshed.shell import execute_js, muterun_js

IO.setwarnings(False)       #do not show any warnings
IO.setmode (IO.BCM)         #we are programming the GPIO by BCM pin numbers. (PIN39 as 'GPIO19')
IO.setup(19,IO.OUT)         # initialize GPIO19 as an output.
IO.setup(26,IO.IN)               #initialize GPIO26 as input
button = Button(26)

# Define host based on hostname -I
# can't find IP address of other thing;
# find before demo, git push and git pull real quick
# run server on pi2

HOST = "192.168.43.7"     # Symbolic name meaning all available interfaces
PORT = 5007               # Arbitrary non-privileged port

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (HOST, PORT)

camera = PiCamera()

# might want to change origin address
origin = '/home/pi/Desktop/project/pictures/origin.jpg'

def take_picture(pic):
    camera.start_preview()
    time.sleep(2)
    camera.capture(pic)
    camera.stop_preview()

while 1:
    IO.output(19, True)
    diff = 0
    button.wait_for_press()
    start_time = time.time()
    
    while button.is_active:
        now_time = time.time()
        diff = -start_time+now_time

    if diff >= 5 :           #long hold
        camera.capture(origin)
        
    else:                   #short hold
        time.sleep(5)

        for i in range(3):
            take_picture('/home/pi/Desktop/project/pictures/'+ str(i) + '.jpg')
        response = muterun_js('mismatch.js')

        if response.exitcode == 0:
            try:
                sock.connect(server_address)
                data = response.stdout
                sock.send(data.encode())
                print('Sending occupancy')
                # turn on LED?
            finally:
                sock.close()
