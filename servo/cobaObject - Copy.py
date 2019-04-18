# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 17:51:29 2019

@author: Binatang Kesusahan
"""
import cv2 as cv
import numpy as np
import imutils
from imutils.video import WebcamVideoStream

class ObjCenter:
    def update(self, frame, framecenter):

        frame =  imutils.resize(frame, width=300)

        gaussian_kernel = int(rw.read("../setting/gaussian_bola.txt"))
        gaussian_kernel = rw.odd(gaussian_kernel)

        frame = cv.GaussianBlur(frame, (gaussian_kernel,gaussian_kernel), 0)
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

        l_h = int(rw.read("../setting/LH.txt"))
        l_s = int(rw.read("../setting/LS.txt"))
        l_v = int(rw.read("../setting/LV.txt"))
        u_h = int(rw.read("../setting/UH.txt"))
        u_s = int(rw.read("../setting/US.txt"))
        u_v = int(rw.read("../setting/UV.txt"))

        lower_white = np.array([l_h,l_s,l_v])
        upper_white = np.array([u_h,u_s,u_v])

        mask = cv.inRange(hsv, lower_white, upper_white)

        erosion = int(rw.read("../setting/erosion_bola.txt"))
        erosion = rw.odd(erosion)

        dilation= int(rw.read("../setting/dilation_bola.txt"))
        dilation= rw.odd(dilation)

        erosion_iterations = int(rw.read("../setting/erosion_iteration_bola.txt"))
        dilation_iterations = int(rw.read("../setting/dilation_iteration_bola.txt"))

        erosion_kernel = cv.getStructuringElement(cv.MORPH_RECT, (erosion, erosion))
        dilation_kernel = cv.getStructuringElement(cv.MORPH_RECT, (dilation, dilation))

        mask = cv.erode(mask, erosion_kernel, iterations = erosion_iterations)
        mask = cv.dilate(mask, dilation_kernel, iterations = dilation_iterations)

        # result = cv.bitwise_and(frame, frame, mask = mask)
        contours, _ = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

        x = 0
        y = 0
        radius = 0

        if len(contours) > 0:
            c = max(contours, key=cv.contourArea)
            ((x, y), radius) = cv.minEnclosingCircle(c)
            M = cv.moments(c)

            if int(M["m00"]) > 0:

                rads = int(rw.read("../setting/radius_bola.txt"))
                if radius > rads :
                    return ((int(x), int(y)))

        return (framecenter)




cap = WebcamVideoStream(0).start()
while True:
    frame = cap.read()

    obj = ObjCenter()
    print(obj.update(frame, (0,0)))
