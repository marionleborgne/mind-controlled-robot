__author__ = 'marion'

import serial
import time

PORT = '/dev/tty.usbmodem1451'
BAUDRATE = 9600

def send_go_foreward():
    ser = serial.Serial(PORT, BAUDRATE)
    for i in range(5):
        ser.write('f')

def send_turn_left():
    ser = serial.Serial(PORT, BAUDRATE)
    ser.write('l')


