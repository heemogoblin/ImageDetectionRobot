#!/usr/bin/python3

from RPi import GPIO
from time import sleep

class LineSensor:
    sensor = 25
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.sensor, GPIO.IN)

    def is_on_line(self):
        return not GPIO.input(self.sensor)

    def __del__(self):
        GPIO.cleanup()