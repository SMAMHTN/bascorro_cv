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

cv.createTrackbar("L - H", "trackbars", 0, 179, cb.LH)
cv.createTrackbar("L - S", "trackbars", 0, 255, cb.LS)
cv.createTrackbar("L - V", "trackbars", 0, 255, cb.LV)
cv.createTrackbar("U - H", "trackbars", 179, 179, cb.UH)
cv.createTrackbar("U - S", "trackbars", 255, 255, cb.US)
cv.createTrackbar("U - V", "trackbars", 255, 255, cb.UV)

while True:
    _, frame = cap.read()
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    hsv = cv.GaussianBlur(hsv, (5,5), 0)
    
    l_h = read("setting/LH.txt")
    l_s = read("setting/LS.txt")
    l_v = read("setting/LV.txt")
    u_h = read("setting/UH.txt")
    u_s = read("setting/US.txt")
    u_v = read("setting/UV.txt")
    
#    l_h = cv.getTrackbarPos("L - H", "trackbars")
    l_s = cv.getTrackbarPos("L - S", "trackbars")
    l_v = cv.getTrackbarPos("L - V", "trackbars")
    u_h = cv.getTrackbarPos("U - H", "trackbars")
    u_s = cv.getTrackbarPos("U - S", "trackbars")
    u_v = cv.getTrackbarPos("U - V", "trackbars")
    
    lower_white = np.array([l_h,l_s,l_v])
    upper_white = np.array([u_h,u_s,u_v])
    
    mask = cv.inRange(hsv, lower_white, upper_white)
#    mask_rumput = 
    
    result = cv.bitwise_and(frame, frame, mask = mask)
    
    key = cv.waitKey(1)
    if key == 27:
        break

cap.release()
cv.destroyAllWindows()