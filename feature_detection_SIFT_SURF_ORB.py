# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 14:47:05 2019

@author: Binatang Kesusahan
"""

import cv2 as cv
import numpy as np

cv.namedWindow("Image", cv.WINDOW_KEEPRATIO)
img = cv.imread("gambar/ujung_kiri.jpg", cv.IMREAD_COLOR)
cv.resizeWindow("Image", 450, 600 )
sift = cv.xfeatures2d.SIFT_create()
surf = cv.xfeatures2d.SURF_create()
orb = cv.ORB_create(nfeatures=500)

#keypoints, descriptor = orb.detectAndCompute(img, None)
#keypoints, descriptor = surf.detectAndCompute(img, None)
keypoints, descriptor = sift.detectAndCompute(img, None)




img = cv.drawKeypoints(img, keypoints, None)

cv.imshow("Image",  img)
cv.waitKey(0)
cv.destroyAllWindows()