# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 13:27:40 2019

@author: Binatang Kesusahan
"""

import cv2 as cv
import numpy as np

#video = cv.VideoCapture("goalpost.mp4")
video = cv.VideoCapture(0)
roi = cv.imread("gambar/tiang_kanan.jpg")
roi = cv.resize(roi , (600,400))
hsv_roi = cv.cvtColor(roi, cv.COLOR_BGR2HSV)
roi_hist = cv.calcHist([hsv_roi], [0], None, [180], [0, 180] )
roi_hist = cv.normalize(roi_hist, roi_hist, 0, 255, cv.NORM_MINMAX)



while True:
    _, frame = video.read()
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    mask = cv.calcBackProject([hsv], [0], roi_hist, [0,180], 1)
    
    cv.imshow("mask", mask)
    cv.imshow("frame", frame)
    
    key = cv.waitKey(80)
    if key == 27:
        break

video.release()
cv.destroyAllWindows()


#
#
#
#roi  = cv.imread("goal_post.jpg")
#hsv_roi = cv.cvtColor(roi, cv.COLOR_BGR2HSV)
#
#roi_hist = cv.calcHist([hsv_roi], [0,1], None, [180,256], [0,180,0,256])
#mask = cv.calcBackProject([hsv_original], [0,1], roi_hist, [0,180,0,256], 1)
#
##filtering remove noise
#kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (5,5))
#mask = cv.filter2D(mask, -1, kernel)
#mask = cv.
#cv.imshow("Original", original_image )
#cv.imshow("roi", roi)
#cv.imshow("mask", mask)
#cv.waitKey(0)
#cv.destroyAllWindows()