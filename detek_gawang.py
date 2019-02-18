# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 17:51:29 2019

@author: Binatang Kesusahan
"""
import cv2 as cv
import numpy as np

def saveConfig(value, file_name):
    value = str(value)
    filename = file_name + ".txt"
    file = open(str(filename), "w")
    file.write(value)
    file.close()

def read(file):
    f = open(file, "r")
    return f.read()  

cap = cv.VideoCapture(0)

cv.namedWindow("trackbars")
cv.createTrackbar("L - H", "trackbars", int(read("setting/LH.txt")), 179, lambda x: saveConfig(x, "setting/LH"))
cv.createTrackbar("L - S", "trackbars", int(read("setting/LS.txt")), 255, lambda x : saveConfig(x, "setting/LS"))
cv.createTrackbar("L - V", "trackbars", int(read("setting/LV.txt")), 255, lambda x : saveConfig(x, "setting/LV"))
cv.createTrackbar("U - H", "trackbars", int(read("setting/UH.txt")), 179, lambda x: saveConfig(x, "setting/UH"))
cv.createTrackbar("U - S", "trackbars", int(read("setting/US.txt")), 255, lambda x: saveConfig(x, "setting/US"))
cv.createTrackbar("U - V", "trackbars", int(read("setting/UV.txt")), 255, lambda x : saveConfig(x, "setting/UV"))


while True:
    ret, frame = cap.read()
    tinggi, panjang, _ = frame.shape
    
    frame = cv.GaussianBlur(frame, (11,11), 0)
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
 
    l_h = int(read("setting/LH.txt"))
    l_s = int(read("setting/LS.txt"))
    l_v = int(read("setting/LV.txt"))
    u_h = int(read("setting/UH.txt"))
    u_s = int(read("setting/US.txt"))
    u_v = int(read("setting/UV.txt"))
    
    lower_white = np.array([l_h,l_s,l_v])   
    upper_white = np.array([u_h,u_s,u_v])
    
    mask = cv.inRange(hsv, lower_white, upper_white)
    mask = cv.erode(mask, (19,19), iterations = 2)
    mask = cv.dilate(mask, (19,19), iterations = 2)
    
    result = cv.bitwise_and(frame, frame, mask = mask)
#    mask_rumput = 
    _, contours, _ = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    
    center = 0
    if len(contours) > 0:
        c = max(contours, key= cv.contourArea)
        ((x,y), radius) = cv.minEnclosingCircle(c)
        M = cv.moments(c)
        
        # untuk calculate centroid
        if M["m00"] > 0:
            cx = int(M["m10"]) / int(M["m00"])
            cy = int(M["m01"]) / int(M["m00"])
        center = (int(cx), int(cy))        
        
        if radius > 5:
            cv.circle(result, (int(x), int(y)), int(radius), (0,255,255), 2)
            cv.circle(result, center, 5, (0,0,255), -1)
            cv.putText(result, "x : {}, y : {}".format(int(cx), int(cy)), (10, tinggi-25), cv.FONT_HERSHEY_COMPLEX_SMALL,0.8, (10,255,10))
            
#   Buat Garis Area di Layar
    cv.line(result, (int(panjang/3), tinggi), (int(panjang/3),0), (0,255,0), 2) #kiri
    cv.line(result, (int(2*panjang/3), tinggi), (int(2*panjang/3),0), (0,255,0), 2) # kanan
    cv.line(result, (0, int(2*tinggi/3)), (panjang, int(2*tinggi/3) ), (123,10,32), 2) #bawah
    
    cv.imshow("result", result)
#    cv.imshow("mask", mask)
#    cv.imshow("frame", frame)
    key = cv.waitKey(1)
    if key == 27:
        break

cap.release()
cv.destroyAllWindows()