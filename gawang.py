import cv2 as cv
import numpy as np
import time

def nothing(x):
    pass

def saveConfig(value, file_name):
    value = str(value)
    filename = file_name + ".txt"
    file = open(str(filename), "w")
    file.write(value)
    file.close()

def read(file):
    f = open(file, "r")
    return f.read()  

cap = cv.VideoCapture(1)
#cap = cv.VideoCapture("goalpost2.mp4")
#cap.set(cv.CAP_PROP_FRAME_WIDTH, 120)
#cap.set(cv.CAP_PROP_FRAME_HEIGHT, 240)

cv.namedWindow("mask_gawang", cv.WINDOW_KEEPRATIO)
cv.resizeWindow("mask_gawang", (600,400))
cv.namedWindow("Gawang", cv.WINDOW_NORMAL)
#cv.resizeWindow("Gawang", 300, 700)
cv.createTrackbar("L - H", "Gawang", int(read("setting/LH_gawang.txt")), 179, lambda x: saveConfig(x, "setting/LH_gawang"))
cv.createTrackbar("L - S", "Gawang", int(read("setting/LS_gawang.txt")), 255, lambda x : saveConfig(x, "setting/LS_gawang"))
cv.createTrackbar("L - V", "Gawang", int(read("setting/LV_gawang.txt")), 255, lambda x : saveConfig(x, "setting/LV_gawang"))
cv.createTrackbar("U - H", "Gawang", int(read("setting/UH_gawang.txt")), 179, lambda x: saveConfig(x, "setting/UH_gawang"))
cv.createTrackbar("U - S", "Gawang", int(read("setting/US_gawang.txt")), 255, lambda x: saveConfig(x, "setting/US_gawang"))
cv.createTrackbar("U - V", "Gawang", int(read("setting/UV_gawang.txt")), 255, lambda x : saveConfig(x, "setting/UV_gawang"))
cv.createTrackbar("Area Gawang", "Gawang", int(read("setting/area_gawang.txt")), 100000, lambda x : saveConfig(x, "setting/area_gawang"))

font = cv.FONT_HERSHEY_SIMPLEX
while True:
    ret, frame = cap.read()

    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
         
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
    #contour detection
    _, contours, _= cv.findContours(mask,cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    
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
            
        rads = int(read("setting/area_gawang.txt"))
        if radius > rads :
#            cv.circle(frame, (int(x), int(y)), int(radius), (0,255,255), 2)
            cv.circle(frame, center, 5, (0,0,255), -1)
            cv.putText(frame, "x : {} y : {}".format(int(cx), int(cy)), (10, frame.shape[0]-25), cv.FONT_HERSHEY_COMPLEX_SMALL,0.8, (10,255,10))
##        time.sleep(0.5)
       
#    for cnt in contours:
#        area = cv.contourArea(cnt)
#        approx = cv.approxPolyDP(cnt,  0.01*cv.arcLength(cnt, True),True)
#        x = approx.ravel()[0]
#        y = approx.ravel()[1]
#        
#        area_gawang = int(read("setting/area_gawang.txt"))
#        if area >area_gawang:
#            
#            if 6 < len(approx) < 9:
#                cv.drawContours(frame, [approx], 0,(0,255,0), 4)
#                cv.putText(frame, "Detected", (x,y), font, 1, (0,200,200))
#    
#        
    cv.imshow("frame", frame)
    cv.imshow("mask_gawang", mask)
        
    key = cv.waitKey(10)
    if key == 27:
        break
    
cap.release()
cv.destroyAllWindows()