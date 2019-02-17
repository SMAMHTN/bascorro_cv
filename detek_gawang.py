# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 17:51:29 2019

@author: Binatang Kesusahan
"""
import cv2 as cv
import numpy as np
import callback as cb


def read(file):
    f = open(file)
    return f.readline()  

cap = cv.VideoCapture(1)
cv.namedWindow("trackbars")

cv.createTrackbar("L - H", "trackbars", int(read("setting/LH.txt")), 179, cb.LH)
cv.createTrackbar("L - S", "trackbars", int(read("setting/LS.txt")), 255, cb.LS)
cv.createTrackbar("L - V", "trackbars", int(read("setting/LV.txt")), 255, cb.LV)
cv.createTrackbar("U - H", "trackbars", int(read("setting/UH.txt")), 179, cb.UH)
cv.createTrackbar("U - S", "trackbars", int(read("setting/US.txt")), 255, cb.US)
cv.createTrackbar("U - V", "trackbars", int(read("setting/UV.txt")), 255, cb.UV)

while True:
    _, frame = cap.read()
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    hsv = cv.GaussianBlur(hsv, (5,5), 0)
    
    l_h = int(read("setting/LH.txt"))
    l_s = int(read("setting/LS.txt"))
    l_v = int(read("setting/LV.txt"))
    u_h = int(read("setting/UH.txt"))
    u_s = int(read("setting/US.txt"))
    u_v = int(read("setting/UV.txt"))
    
#    l_h = cv.getTrackbarPos("L - H", "trackbars")
#    l_s = cv.getTrackbarPos("L - S", "trackbars")
#    l_v = cv.getTrackbarPos("L - V", "trackbars")
#    u_h = cv.getTrackbarPos("U - H", "trackbars")
#    u_s = cv.getTrackbarPos("U - S", "trackbars")
#    u_v = cv.getTrackbarPos("U - V", "trackbars")
    
    lower_white = np.array([l_h,l_s,l_v])
    upper_white = np.array([u_h,u_s,u_v])
    
    mask = cv.inRange(hsv, lower_white, upper_white)
#    mask_rumput = 
    
    result = cv.bitwise_and(frame, frame, mask = mask)
    cv.imshow("result", result)
    key = cv.waitKey(1)
    if key == 27:
        break

cap.release()
cv.destroyAllWindows()