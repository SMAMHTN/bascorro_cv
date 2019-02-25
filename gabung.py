# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 21:21:46 2019

@author: Binatang Kesusahan
"""
import cv2 as cv
import numpy as np
import imutils
#import time

##############################################################################################################################################
def saveConfig(value, file_name):
    value = str(value)
    filename = file_name + ".txt"
    file = open(str(filename), "w")
    file.write(value)
    file.close()
##############################################################################################################################################
def read(file):
    f = open(file, "r")
    return f.read()

  
def gawang(frame):
    
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
         
    l_h_gawang = int(read("setting/LH_gawang.txt"))
    l_s_gawang = int(read("setting/LS_gawang.txt"))
    l_v_gawang = int(read("setting/LV_gawang.txt"))
    u_h_gawang = int(read("setting/UH_gawang.txt"))
    u_s_gawang = int(read("setting/US_gawang.txt"))
    u_v_gawang = int(read("setting/UV_gawang.txt"))
    
    lower_color = np.array([l_h_gawang, l_s_gawang, l_v_gawang])
    upper_color = np.array([u_h_gawang, u_s_gawang ,u_v_gawang])
    
    mask_gawang = cv.inRange(hsv, lower_color, upper_color)
    kernel = np.ones((5,5), np.uint8)
    
    mask_gawang = cv.erode(mask_gawang, kernel)
    
    _, contours, _= cv.findContours(mask,cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    
    if len(contours) > 0:
        c = max(contours, key= cv.contourArea)
        ((x,y), radius) = cv.minEnclosingCircle(c)
        M = cv.moments(c)
        
        # calculate centroid
        if int(M["m00"])> 0:
            cx = int(M["m10"]) / int(M["m00"])
            cy = int(M["m01"]) / int(M["m00"])
            center = (int(cx), int(cy))        
        else:
            center = (1,1)
            
        rads = int(read("setting/radius.txt"))
        if radius > rads :
            cv.circle(frame, center, 5, (0,0,255), -1)
            cv.putText(frame, "x : {} y : {}".format(int(cx), int(cy)), (10, frame.shape[0]-25), cv.FONT_HERSHEY_COMPLEX_SMALL,0.8, (10,255,10))
    
    cv.imshow("frame", frame)
    cv.imshow("mask_gawang", mask_gawang)
   
    
cap = cv.VideoCapture(0)
cap.set(cv.CAP_PROP_FRAME_WIDTH, 120)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, 240)
##############################################################################################################################################
cv.namedWindow("trackbars", cv.WINDOW_NORMAL)
cv.resizeWindow("trackbars", 300, 700)
cv.createTrackbar("L - H", "trackbars", int(read("setting/LH.txt")), 179, lambda x: saveConfig(x, "setting/LH"))
cv.createTrackbar("L - S", "trackbars", int(read("setting/LS.txt")), 255, lambda x : saveConfig(x, "setting/LS"))
cv.createTrackbar("L - V", "trackbars", int(read("setting/LV.txt")), 255, lambda x : saveConfig(x, "setting/LV"))
cv.createTrackbar("U - H", "trackbars", int(read("setting/UH.txt")), 179, lambda x: saveConfig(x, "setting/UH"))
cv.createTrackbar("U - S", "trackbars", int(read("setting/US.txt")), 255, lambda x: saveConfig(x, "setting/US"))
cv.createTrackbar("U - V", "trackbars", int(read("setting/UV.txt")), 255, lambda x : saveConfig(x, "setting/UV"))
#Trackbar untuk dilation, erosion, gausian
cv.createTrackbar("dilation", "trackbars", int(read("setting/dilation.txt")), 50, lambda x : saveConfig(x, "setting/dilation"))	
cv.createTrackbar("DIL iterations", "trackbars", int(read("setting/dilation_iterations.txt")), 50, lambda x : saveConfig(x, "setting/dilation_iterations"))
cv.createTrackbar("erosion", "trackbars", int(read("setting/erosion.txt")), 50, lambda x : saveConfig(x, "setting/erosion"))
cv.createTrackbar("ER iterations", "trackbars", int(read("setting/erosion_iterations.txt")), 50, lambda x : saveConfig(x, "setting/erosion_iterations"))
#OPENING
cv.createTrackbar("opening\r\n kernel\r\n size", "trackbars", int(read("setting/opening.txt")), 100, lambda x : saveConfig(x, "setting/opening"))
cv.createTrackbar("kernel\r\n type", "trackbars", int(read("setting/opening_kernel_type.txt")), 2, lambda x : saveConfig(x, "setting/opening_kernel_type"))
cv.createTrackbar("opening\r\n iterations", "trackbars", int(read("setting/opening_iterations.txt")), 200, lambda x : saveConfig(x, "setting/opening_iterations"))
cv.createTrackbar("gaussian", "trackbars", int(read("setting/gaussian.txt")), 200, lambda x : saveConfig(x, "setting/gaussian"))

#trackbar untuk setting radius di bola
cv.createTrackbar("radius", "trackbars", int(read("setting/radius.txt")), 200, lambda x : saveConfig(x, "setting/radius"))

# trackbar gawang
cv.namedWindow("mask_gawang", cv.WINDOW_KEEPRATIO)
cv.resizeWindow("mask_gawang", (600,400))
cv.namedWindow("Gawang", cv.WINDOW_NORMAL)
cv.resizeWindow("Gawang", 300, 700)
cv.createTrackbar("L - H", "Gawang", int(read("setting/LH_gawang.txt")), 179, lambda x: saveConfig(x, "setting/LH_gawang"))
cv.createTrackbar("L - S", "Gawang", int(read("setting/LS_gawang.txt")), 255, lambda x : saveConfig(x, "setting/LS_gawang"))
cv.createTrackbar("L - V", "Gawang", int(read("setting/LV_gawang.txt")), 255, lambda x : saveConfig(x, "setting/LV_gawang"))
cv.createTrackbar("U - H", "Gawang", int(read("setting/UH_gawang.txt")), 179, lambda x: saveConfig(x, "setting/UH_gawang"))
cv.createTrackbar("U - S", "Gawang", int(read("setting/US_gawang.txt")), 255, lambda x: saveConfig(x, "setting/US_gawang"))
cv.createTrackbar("U - V", "Gawang", int(read("setting/UV_gawang.txt")), 255, lambda x : saveConfig(x, "setting/UV_gawang"))
cv.createTrackbar("Area Gawang", "Gawang", int(read("setting/area_gawang.txt")), 100000, lambda x : saveConfig(x, "setting/area_gawang"))


##############################################################################################################################################
while True:
    
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
    
    lower_ball = np.array([l_h,l_s,l_v])   
    upper_ball = np.array([u_h,u_s,u_v])
    
    mask = cv.inRange(hsv, lower_ball, upper_ball)
 
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
#################################################################################################################
    erosion_iterations = int(read("setting/erosion_iterations.txt"))
    dilation_iterations = int(read("setting/dilation_iterations.txt"))
    
    erosion_kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (erosion, erosion))
    dilation_kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (dilation, dilation))
    
    mask = cv.erode(mask, erosion_kernel, iterations = erosion_iterations)
    mask = cv.dilate(mask, dilation_kernel, iterations = dilation_iterations)
    
    result = cv.bitwise_and(frame, frame, mask = mask)
    
    _, contours, _ = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    
    center = 0
    if len(contours) > 0:
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
            
        rads = int(read("setting/radius.txt"))
        if radius > rads :
            
            if x < panjang/3 and y < 2*tinggi/3:
                cv.putText(result, "KIRI ATAS", (10, tinggi - 40), cv.FONT_HERSHEY_SIMPLEX, 0.5, (100,255,10), 1)
                gawang(frame)
                
                
            elif x < 2*panjang/3 and y < 2*tinggi/3:
                cv.putText(result, "TENGAH ATAS", (10, tinggi - 40), cv.FONT_HERSHEY_SIMPLEX, 0.5, (100,250,10),1)
                gawang(frame)
                
            elif x > 2*panjang/3 and y < 2*tinggi/3:
                cv.putText(result, "KANAN ATAS", (10, tinggi - 40), cv.FONT_HERSHEY_SIMPLEX, 0.5, (100,250,10),1)
                gawang(frame)
                
            
            cv.circle(result, (int(x), int(y)), int(radius), (0,255,255), 2)
            cv.circle(result, center, 5, (0,0,255), -1)
            cv.putText(result, "x : {} y : {}".format(int(cx), int(cy)), (10, tinggi-25), cv.FONT_HERSHEY_COMPLEX_SMALL,0.8, (10,255,10))
##############################################################################################################################################
#   Buat Garis Area di Layar
    cv.line(result, (int(panjang/3), tinggi), (int(panjang/3),0), (0,255,0), 2) #kiri
    cv.line(result, (int(2*panjang/3), tinggi), (int(2*panjang/3),0), (0,255,0), 2) # kanan
    cv.line(result, (0, int(2*tinggi/3)), (panjang, int(2*tinggi/3) ), (123,10,32), 2) #bawah
    
    
    cv.imshow("result", result)
    cv.imshow("mask", mask)
#    cv.imshow("frame", frame)
##############################################################################################################################################
    
    key = cv.waitKey(1)
    if key == 27:
        break
cap.release()
cv.destroyAllWindows()