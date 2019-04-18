from multiprocessing import Manager
from multiprocessing import Process
from imutils.video import WebcamVideoStream
import imutils
from servo.cobaObject import ObjCenter
from servo.pid import PID
import argparse
import signal
import time
import sys
import cv2 as cv
import servo.servoControl as sc

panServoRange = (-90, 90)
tiltServoRange = (-70, 70)
panServo = 27
tiltServo = 17

def signal_handler(sig, frame):
    print("[INFO] ctrl + c pressed, exiting...")

    # sc.disableServo(panServo)
    # sc.disableServo(tiltServo)

    sys.exit()


def obj_center(objX, objY, centerX, centerY):
    signal.signal(signal.SIGINT, signal_handler)

    vs = WebcamVideoStream(args.camera).start()
    # time.sleep(2.0)

    obj = ObjCenter()

    while True:
        frame = vs.read()
        frame = imutils.resize(frame,width=300)
        (H, W, _) = frame.shape
        centerX.value = W // 2
        centerY.value = H // 2

        objectLoc = obj.update(frame, (centerX.value, centerY.value))
        (objX.value, objY.value) = objectLoc
        cv.imshow("frame", frame)
        print(objectLoc)
        cv.waitKey(1)
    vs.stop()

def pid_process(output, p, i, d, objCoord, centerCoord):
    signal.signal(signal.SIGINT, signal_handler)

    p = PID(p.value, i.value, d.value)
    p.initialize()

    while True:

        error =  centerCoord.value - objCoord.value

        output.value = p.update(error)

def in_range(val,  start, end):
    return (val >= start and val <= end)

def set_servos(pan, tlt):
    signal.signal(signal.SIGINT, signal_handler)

    while True:
        panAngle = -1 * pan.value
        tiltAngle = -1 * tlt.value

        if in_range(panAngle, panServoRange[0], panServoRange[1]):
            sc.setServoAngle(panServo,panAngle)

        if in_range(tiltAngle, tiltServoRange[0], tiltServoRange[1]):
            sc.setServoAngle(tiltServo, tiltAngle)

if __name__ == "__main__":
    ap = argparse.ArgumentParser()

    ap.add_argument("-c", "--camera", type=int, default=0, help="change camera")

    args = ap.parse_args()


    with Manager() as manager:
        centerX = manager.Value("i", 0)
        centerY = manager.Value("i", 0)

        objX = manager.Value("i", 0)
        objY = manager.Value("i", 0)

        pan = manager.Value("i", 0)
        tlt = manager.Value("i", 0)

        panP = manager.Value("f", 0.09)
        panI = manager.Value("f", 0.08)
        panD = manager.Value("f", 0.002)

        tiltP = manager.Value("f", 0.11)
        tiltI = manager.Value("f", 0.10)
        tiltD = manager.Value("f", 0.002)

        processObjectCenter = Process(target=obj_center, args=(objX, objY, centerX, centerY) )
        processPanning = Process(target=pid_process, args=(pan, panP, panI, panD, objX, centerX))
        processTilting = Process(target=pid_process, args=(tlt, tiltP, tiltI, tiltD, objY, centerY))
        processSetServos = Process(target=set_servos, args=(pan, tlt))

        processObjectCenter.start()
        # processPanning.start()
        processTilting.start()
        processSetServos.start()

        processObjectCenter.join()
        # processPanning.join()
        processTilting.join()
        processSetServos.join()

        # sc.disableServo(panServo)
        # sc.disableServo(tiltServo)