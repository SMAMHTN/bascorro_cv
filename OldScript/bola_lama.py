# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 17:51:29 2019

@author: Binatang Kesusahan
"""
import cv2 as cv
import numpy as np
import imutils
import rw_file as rw

import time
import serial as Serial
from save_load import read as read
from save_load import saveConfig as saveConfig

def serial(posisi):
    ser = Serial('/dev/ttyUSB0',)
    ser.baudrate = 115200
    
    while 1:
        if (posisi == '1'):
            ser.write(str(1).encode())
            print('kiri, 101')
            time.sleep(0.1)
            ser.write(str(0).encode())
            time.sleep(0.1)
            ser.write(str(1).encode())
            
        elif (posisi == '2'):
            print('kiri, nyala 1010 x')
            ser.write(str(1).encode())
            time.sleep(0.1)
            ser.write(str(0).encode())
            ser.write(str(1).encode())
            time.sleep(0.1)
            ser.write(str(0).encode())
            
        elif (posisi == '3'):
            ser.write(str(1).encode())
            time.sleep(0.1)
            ser.write(str(0).encode())
            time.sleep(0.1)
            ser.write(str(1).encode())
            time.sleep(0.1)
            ser.write(str(0).encode())
            time.sleep(0.1)
            ser.write(str(1).encode())
            time.sleep(0.1)
            ser.write(str(0).encode())
            
        
    print(ser.readline())
    return 0

def centroid(contours):
#    center =0
#    cx =0 
#    cy =0
    
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


def gawang(hsv):
    
    l_h = int(read("setting/LH_gawang.txt"))
    l_s = int(read("setting/LS_gawang.txt"))
    l_v = int(read("setting/LV_gawang.txt"))
    u_h = int(read("setting/UH_gawang.txt"))
    u_s = int(read("setting/US_gawang.txt"))
    u_v = int(read("setting/UV_gawang.txt"))
    
    lower_color = np.array([l_h,l_s,l_v])
    upper_color = np.array([u_h,u_s,u_v])
    
    mask = cv.inRange(hsv, lower_color, upper_color)
    kernel = np.ones((5,5), np.uint8)
    
    mask = cv.erode(mask, kernel)
    
    _, contours, _ = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
   
    if len(contours) > 0:
        radius_gawang, center_gawang, cx_gawang, cy_gawang, _, _ = centroid(contours)
        return(radius_gawang, center_gawang, cx_gawang, cy_gawang)
    
    
cap = cv.VideoCapture(0)
cap.set(cv.CAP_PROP_FRAME_WIDTH, 120)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, 240)

cv.namedWindow("trackbars", cv.WINDOW_NORMAL)
cv.resizeWindow("trackbars", 300, 500)
cv.createTrackbar("L - H", "trackbars", int(rw.read("setting/LH.txt")), 179, lambda x: rw.write(x, "setting/LH.txt"))
cv.createTrackbar("L - S", "trackbars", int(rw.read("setting/LS.txt")), 255, lambda x : rw.write(x, "setting/LS.txt"))
cv.createTrackbar("L - V", "trackbars", int(rw.read("setting/LV.txt")), 255, lambda x : rw.write(x, "setting/LV.txt"))
cv.createTrackbar("U - H", "trackbars", int(rw.read("setting/UH.txt")), 179, lambda x: rw.write(x, "setting/UH.txt"))
cv.createTrackbar("U - S", "trackbars", int(rw.read("setting/US.txt")), 255, lambda x: rw.write(x, "setting/US.txt"))
cv.createTrackbar("U - V", "trackbars", int(rw.read("setting/UV.txt")), 255, lambda x : rw.write(x, "setting/UV.txt"))

cv.createTrackbar("dilation", "trackbars", int(rw.read("setting/dilation_bola.txt")), 50, lambda x : rw.write(x, "setting/dilation_bola.txt"))
cv.createTrackbar("Dilation iterations", "trackbars", int(rw.read("setting/dilation_iteration_bola.txt")), 200, lambda x : rw.write(x, "setting/dilation_iteration_bola.txt"))
cv.createTrackbar("erosion", "trackbars", int(rw.read("setting/erosion_bola.txt")), 50, lambda x : rw.write(x, "setting/erosion_bola.txt"))
cv.createTrackbar("Erosion iterations", "trackbars", int(rw.read("setting/erosion_iteration_bola.txt")), 200, lambda x : rw.write(x, "setting/erosion_iteration_bola.txt"))
cv.createTrackbar("gaussian", "trackbars", int(rw.read("setting/gaussian_bola.txt")), 20, lambda x : rw.write(x, "setting/gaussian_bola.txt"))
cv.createTrackbar("radius", "trackbars", int(rw.read("setting/radius_bola.txt")), 50, lambda x : rw.write(x, "setting/radius_bola.txt"))



while True:
    ret, frame = cap.read()
    frame =  imutils.resize(frame, width=300)
    tinggi, panjang, _ = frame.shape

    gaussian_kernel = int(rw.read("setting/gaussian_bola.txt"))
    if gaussian_kernel == 0:
        gaussian_kernel = 1
    else:
        gaussian_kernel = (2*gaussian_kernel)+1

    frame = cv.GaussianBlur(frame, (gaussian_kernel,gaussian_kernel), 0)
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    l_h = int(rw.read("setting/LH.txt"))
    l_s = int(rw.read("setting/LS.txt"))
    l_v = int(rw.read("setting/LV.txt"))
    u_h = int(rw.read("setting/UH.txt"))
    u_s = int(rw.read("setting/US.txt"))
    u_v = int(rw.read("setting/UV.txt"))

    lower_white = np.array([l_h,l_s,l_v])
    upper_white = np.array([u_h,u_s,u_v])

    mask = cv.inRange(hsv, lower_white, upper_white)

    erosion = int(rw.read("setting/erosion_bola.txt"))

    if erosion == 0:
        erosion = 1
    else:
        erosion = (2*erosion)+1

    dilation= int(rw.read("setting/dilation_bola.txt"))
    if dilation == 0:
        dilation = 1
    else:
        dilation = (2*dilation)+1

    erosion_iterations = int(rw.read("setting/erosion_iteration_bola.txt"))
    dilation_iterations = int(rw.read("setting/dilation_iteration_bola.txt"))

    erosion_kernel = cv.getStructuringElement(cv.MORPH_RECT, (erosion, erosion))
    dilation_kernel = cv.getStructuringElement(cv.MORPH_RECT, (dilation, dilation))

    mask = cv.erode(mask, erosion_kernel, iterations = erosion_iterations)
    mask = cv.dilate(mask, dilation_kernel, iterations = dilation_iterations)

    result = cv.bitwise_and(frame, frame, mask = mask)

    contours, _ = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    x = 0
    y = 0
    radius = 0
    center_gawang = 0
    radius_gawang = 0
    cx_gawang = 0
    cy_gawang = 0

    rads_gawang = int(read("setting/area_gawang.txt"))
    
    if len(contours) > 0:
        radius, center, cx, cy, x, y = centroid(contours)
        
        rads = int(read("setting/radius.txt"))
        if radius > rads :
            
            if x < panjang/3 and y < 2*tinggi/3:
                print("kiri atas")
                posisi = 1
#                serial(posisi)
                radius_gawang, center_gawang, cx_gawang, cy_gawang = gawang(hsv)
                if radius_gawang > rads_gawang:
                    cv.circle(result, center_gawang, 5, (0,0,255), -1)
                    cv.putText(result, "x : {} y : {}".format(int(cx_gawang), int(cy_gawang)), (10, frame.shape[0]-70), cv.FONT_HERSHEY_COMPLEX_SMALL,0.8, (10,255,10))
                cv.putText(result, "KIRI ATAS", (10, tinggi - 40), cv.FONT_HERSHEY_SIMPLEX, 0.5, (100,255,10), 1)
            
            elif x < 2*panjang/3 and y < 2*tinggi/3:
                print("tengah atas")
                posisi = 2
#                serial(posisi)
                radius_gawang, center_gawang, cx_gawang, cy_gawang = gawang(hsv)
                if radius_gawang > rads_gawang:
                    cv.circle(result, center_gawang, 5, (0,0,255), -1)
                    cv.putText(result, "x : {} y : {}".format(int(cx_gawang), int(cy_gawang)), (10, frame.shape[0]-70), cv.FONT_HERSHEY_COMPLEX_SMALL,0.8, (10,255,10))
                cv.putText(result, "TENGAH ATAS", (10, tinggi - 40), cv.FONT_HERSHEY_SIMPLEX, 0.5, (100,250,10),1)
                
            elif x > 2*panjang/3 and y < 2*tinggi/3:
                print("kanan atas")
                posisi = 3
#                serial(posisi)
                radius_gawang, center_gawang, cx_gawang, cy_gawang = gawang(hsv)
                if radius_gawang > rads_gawang:
                    cv.circle(result, center_gawang, 5, (0,0,255), -1)
                    cv.putText(result, "x : {} y : {}".format(int(cx_gawang), int(cy_gawang)), (10, frame.shape[0]-70), cv.FONT_HERSHEY_COMPLEX_SMALL,0.8, (10,255,10))
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


    x = 0
    y = 0
    radius = 0
    center = None

    if len(contours) > 0:
        c = max(contours, key=cv.contourArea)
        ((x, y), radius) = cv.minEnclosingCircle(c)
        M = cv.moments(c)

        cx = None
        cy = None

        if int(M["m00"]) > 0:
            cx = int(M["m10"]) / int(M["m00"])
            cy = int(M["m01"]) / int(M["m00"])
            center = (int(cx), int(cy))

    rads = int(rw.read("setting/radius_bola.txt"))
    if radius > rads :

        cv.circle(result, (int(x), int(y)), int(radius), (0,255,255), 2)
        cv.circle(result, center, 5, (0,0,255), -1)
        cv.putText(result, "x : {} y : {}".format(int(x), int(y)), (10, tinggi-25), cv.FONT_HERSHEY_COMPLEX_SMALL,0.8, (10,255,10))

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
