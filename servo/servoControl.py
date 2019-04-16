import RPi.GPIO as GPIO
import argparse
import os

panServo = 27
tiltServo = 17

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

def positionServo(servo, angle):
    os.system("python angleServoCtrl " + str(servo) + " " + str(angle))

def mapServoPosition(x, y):
    global panAngle
    global tiltAngle

    if