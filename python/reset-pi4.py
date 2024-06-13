#!/usr/bin/python

# Reset the modem HAT on a Raspberry Pi 4

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.OUT)
GPIO.output(25, GPIO.LOW)
time.sleep(0.5)
GPIO.output(25, GPIO.HIGH)
time.sleep(0.3)
