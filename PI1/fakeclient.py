from gpiozero import Button
import RPi.GPIO as IO
import time
import socket
from signal import pause
import os
from Naked.toolshed.shell import execute_js, muterun_js

HOST = "192.168.43.158"     # Symbolic name meaning all available interfaces
PORT = 5007               # Arbitrary non-privileged port

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (HOST, PORT)
sock.connect(server_address)

try:
    data = "50"
    sock.send(data.encode())
                # turn on LED?
finally:
    sock.close()
