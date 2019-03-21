# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 23:17:54 2019

@author: Binatang Kesusahan
"""
import cv2 as cv
from save_load import read as read
from save_load import saveConfig as saveConfig

cv.namedWindow("trackbars", cv.WINDOW_NORMAL)
cv.resizeWindow("trackbars", 300, 500)
cv.createTrackbar("L - H", "trackbars", int(read("setting/LH.txt")), 179, lambda x: saveConfig(x, "setting/LH"))
cv.createTrackbar("L - S", "trackbars", int(read("setting/LS.txt")), 255, lambda x : saveConfig(x, "setting/LS"))
cv.createTrackbar("L - V", "trackbars", int(read("setting/LV.txt")), 255, lambda x : saveConfig(x, "setting/LV"))
cv.createTrackbar("U - H", "trackbars", int(read("setting/UH.txt")), 179, lambda x: saveConfig(x, "setting/UH"))
cv.createTrackbar("U - S", "trackbars", int(read("setting/US.txt")), 255, lambda x: saveConfig(x, "setting/US"))
cv.createTrackbar("U - V", "trackbars", int(read("setting/UV.txt")), 255, lambda x : saveConfig(x, "setting/UV"))
#Trackbar untuk dilation, erosion, gausian
cv.createTrackbar("dilation", "trackbars", int(read("setting/dilation.txt")), 100, lambda x : saveConfig(x, "setting/dilation"))	
cv.createTrackbar("DIL iterations", "trackbars", int(read("setting/dilation_iterations.txt")), 200, lambda x : saveConfig(x, "setting/dilation_iterations"))
cv.createTrackbar("erosion", "trackbars", int(read("setting/erosion.txt")), 100, lambda x : saveConfig(x, "setting/erosion"))
cv.createTrackbar("ER iterations", "trackbars", int(read("setting/erosion_iterations.txt")), 200, lambda x : saveConfig(x, "setting/erosion_iterations"))
cv.createTrackbar("gaussian", "trackbars", int(read("setting/gaussian.txt")), 200, lambda x : saveConfig(x, "setting/gaussian"))
#trackbar untuk setting radius di bola
cv.createTrackbar("radius", "trackbars", int(read("setting/radius.txt")), 200, lambda x : saveConfig(x, "setting/radius"))
