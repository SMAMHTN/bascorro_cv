# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 21:15:30 2019

@author: Binatang Kesusahan
"""

import cv2 as cv
import numpy as np

#img = cv.imread("goal_post.jpg", cv.IMREAD_GRAYSCALE) #query image
img = cv.imread("gambar/original_image.jpg", cv.IMREAD_GRAYSCALE) #query image
img = cv.resize(img, (640,480))

cap = cv.VideoCapture(0)
#cap = cv.VideoCapture(0)
# Feautures
sift = cv.xfeatures2d.SIFT_create()
kp_image, desc_image = sift.detectAndCompute(img, None)
#img = cv.drawKeypoints(img, kp_image, img)

# Features Matching
index_params = dict(algorithm = 0,  trees = 5)
search_params = dict()
flann = cv.FlannBasedMatcher(index_params, search_params)


while True:
    ret, frame = cap.read()
    if  not ret:
        cap = cv.VideoCapture("goalpost.mp4")             
        continue  
    grayframe = cv.cvtColor(frame, cv.COLOR_BGR2GRAY) #train image
    
    kp_grayframe, desc_grayframe = sift.detectAndCompute(grayframe, None)
#    grayframe = cv.drawKeypoints(grayframe, kp_grayframe, grayframe)
    
    matches = flann.knnMatch(desc_image, desc_grayframe,  k = 2)
    
    good_points = []
    for m, n  in matches:
        if m.distance < 0.8*n.distance:
            good_points.append(m)
    
#    img3 = cv.drawMatches(img, kp_image, grayframe, kp_grayframe, good_points, grayframe)
     
    # Homography
    if len(good_points) > 10:
        query_pts = np.float32([kp_image[m.queryIdx].pt for m in good_points]).reshape(-1, 1, 2)
        train_pts = np.float32([kp_grayframe[m.trainIdx].pt for m in good_points]).reshape(-1, 1, 2)
        
        matrix , mask = cv.findHomography(query_pts, train_pts, cv.RANSAC, 5.0)
        match_mask = mask.ravel().tolist()
        
        #perspective transform
        h, w = img.shape
        pts = np.float32([[0,0], [0,h], [w,h], [w,0]]).reshape(-1,1,2)
        dst = cv.perspectiveTransform(pts, matrix)
        
        homography = cv.polylines(frame, [np.int32(dst)], True, (255,0,0), 3)
        
        cv.imshow("homography", homography)
    else:
        cv.imshow("homography", grayframe)
      
    
#    cv.imshow("image", img)
#    cv.imshow("image3", img3)
#    cv.imshow("gray frame", grayframe)
    
    
    key = cv.waitKey(1)
    if key == 27:
        break
    
cap.release()
cv.destroyAllWindows()
