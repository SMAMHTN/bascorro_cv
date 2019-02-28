# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 17:51:29 2019

@author: Binatang Kesusahan
"""
import cv2 as cv
import numpy as np
import imutils
import time

def centroid(contours):
    center =0
    cx =0 
    cy =0
    
    c = max(contours, key= cv.contourArea)
    ((x,y), radius) = cv.minEnclosingCircle(c)
    M = cv.moments(c)
    
    # untuk calculate centroid
    if int(M["m00"])> 0:
        cx = int(M["m10"]) / int(M["m00"])
        cy = int(M["m01"]) / int(M["m00"])
        center = (int(cx), int(cy))        
    else:
        center = (1,1)
    
    return(radius,center, cx, cy,x,y)
    

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
#cap.set(cv.CAP_PROP_FRAME_WIDTH, 120)
#cap.set(cv.CAP_PROP_FRAME_HEIGHT, 240)

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

while True:
    start = time.time()
    ret, frame = cap.read()
    frame =  imutils.resize(frame, width=600)
    
    tinggi, panjang, _ = frame.shape
    
    gaussian_kernel = int(read("setting/gaussian.txt"))
    if gaussian_kernel == 0:
        gaussian_kernel = 1
    else:
        gaussian_kernel = (2*gaussian_kernel)+1
    
    frame = cv.GaussianBlur(frame, (gaussian_kernel,gaussian_kernel), 0)
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
    
    erosion = int(read("setting/erosion.txt"))
    if erosion == 0:
        erosion = 1 
    else:
        erosion = (2*erosion)+1
        
    dilation= int(read("setting/dilation.txt"))
    if dilation == 0:
        dilation = 1
    else:
        dilation = (2*dilation)+1

    erosion_iterations = int(read("setting/erosion_iterations.txt"))
    dilation_iterations = int(read("setting/dilation_iterations.txt"))
    
    erosion_kernel = cv.getStructuringElement(cv.MORPH_RECT, (erosion, erosion))
    dilation_kernel = cv.getStructuringElement(cv.MORPH_RECT, (dilation, dilation))
    
    mask = cv.erode(mask, erosion_kernel, iterations = erosion_iterations)
    mask = cv.dilate(mask, dilation_kernel, iterations = dilation_iterations)
    
    result = cv.bitwise_and(frame, frame, mask = mask)

    _, contours, _ = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    
    x = 0
    y = 0
    radius = 0
    if len(contours) > 0:
        radius, center, cx, cy, x, y = centroid(contours)
        
        rads = int(read("setting/radius.txt"))
        if radius > rads :
            
            if x < panjang/3 and y < 2*tinggi/3:
                print("kiri atas")
                cv.putText(result, "KIRI ATAS", (10, tinggi - 40), cv.FONT_HERSHEY_SIMPLEX, 0.5, (100,255,10), 1)
            elif x < 2*panjang/3 and y < 2*tinggi/3:
                print("tengah atas")
                cv.putText(result, "TENGAH ATAS", (10, tinggi - 40), cv.FONT_HERSHEY_SIMPLEX, 0.5, (100,250,10),1)
            elif x > 2*panjang/3 and y < 2*tinggi/3:
                print("kanan atas")
                cv.putText(result, "KANAN ATAS", (10, tinggi - 40), cv.FONT_HERSHEY_SIMPLEX, 0.5, (100,250,10),1)
            
        cv.circle(result, (int(x), int(y)), int(radius), (0,255,255), 2)
        cv.circle(result, center, 5, (0,0,255), -1)
        cv.putText(result, "x : {} y : {}".format(int(cx), int(cy)), (10, tinggi-25), cv.FONT_HERSHEY_COMPLEX_SMALL,0.8, (10,255,10))
            
    end = time.time()
    fps = str(int(1/(end-start)))
    cv.putText(result, fps, (10, tinggi-55), cv.FONT_HERSHEY_COMPLEX_SMALL,0.8, (10,255,10))
#   Buat Garis Area di Layar
    cv.line(result, (int(panjang/3), tinggi), (int(panjang/3),0), (0,255,0), 2) #kiri
    cv.line(result, (int(2*panjang/3), tinggi), (int(2*panjang/3),0), (0,255,0), 2) # kanan
    cv.line(result, (0, int(2*tinggi/3)), (panjang, int(2*tinggi/3) ), (123,10,32), 2) #bawah
    
    
    cv.imshow("result", result)
    cv.imshow("mask", mask)
    cv.imshow("frame", frame)
    key = cv.waitKey(1)
    if key == 27:
        break

cap.release()
cv.destroyAllWindows()