import RPi.GPIO as GPIO
from time import sleep
import argparse
import os

panServo = 27
tiltServo = 17

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)


panAngle = 90
tiltAngle = 90


# def positionServo(servo, angle):
#     os.system("python angleServoCtrl " + str(servo) + " " + str(angle))


def setServoAngle(servo, angle):
    GPIO.setup(servo,GPIO.OUT)
    pwm = GPIO.PWM(servo, 50)
    pwm.start(8)
    dutyCycle = (9.8*angle/180) + 2.
    pwm.ChangeDutyCycle(dutyCycle)
    sleep(0.3)
    pwm.stop()

def mapServoPosition(x, y):
    global tiltAngle
    global panAngle
    if (x < 100):
        panAngle +=10
        if panAngle > 140:
            panAngle = 140
        setServoAngle(panServo, panAngle )

    if (x > 200):
        panAngle -=10
        if panAngle < 40:
            panAngle = 40
        setServoAngle(panServo, panAngle)

    if (y < 85):
        tiltAngle += 10
        if tiltAngle > 140:
            tiltAngle = 140
        setServoAngle(tiltServo, tiltAngle)

    if (y > 170):
        tiltAngle -= 10
        if tiltAngle < 40:
            tiltAngle = 40
        setServoAngle(tiltServo, tiltAngle)



setServoAngle(panServo, panAngle)
setServoAngle(tiltServo, tiltAngle)
