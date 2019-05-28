import rw_file as rw
import cv2 as cv
import imutils
from imutils.video import WebcamVideoStream
import numpy as np
import argparse




l_h_gawang = int(rw.read("setting/LH_gawang.txt"))
l_s_gawang = int(rw.read("setting/LS_gawang.txt"))
l_v_gawang = int(rw.read("setting/LV_gawang.txt"))
u_h_gawang = int(rw.read("setting/UH_gawang.txt"))
u_s_gawang = int(rw.read("setting/US_gawang.txt"))
u_v_gawang = int(rw.read("setting/UV_gawang.txt"))

lower_white = np.array([l_h_gawang,l_s_gawang,l_v_gawang])
upper_white = np.array([u_h_gawang,u_s_gawang,u_v_gawang])

dilation_gawang= rw.odd(int(rw.read("setting/dilation_gawang.txt")))
dilation_iteration_gawang = int(rw.read("setting/dilation_iteration_gawang.txt"))
erosion_gawang = rw.odd(int(rw.read("setting/erosion_gawang.txt")))
erosion_iteration_gawang = int(rw.read("setting/erosion_iteration_gawang.txt"))
gaussian_gawang = rw.odd(int(rw.read("setting/gaussian_gawang.txt")))
radius_gawang = int(rw.read("setting/radius_gawang.txt"))

erosion_kernel = cv.getStructuringElement(cv.MORPH_RECT, (erosion_gawang, erosion_gawang))
dilation_kernel = cv.getStructuringElement(cv.MORPH_RECT, (dilation_gawang, dilation_gawang))

def color_filter(frame):
    frame = cv.GaussianBlur(frame, (gaussian_gawang, gaussian_gawang), 0)
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    mask = cv.inRange(hsv, lower_white, upper_white)
    mask = cv.erode(mask, erosion_kernel, iterations=erosion_iteration_gawang)
    mask = cv.dilate(mask, dilation_kernel, iterations=dilation_iteration_gawang)
    result = cv.bitwise_and(frame, frame, mask=mask)
    return result

def canny(frame):
    pass

def hough(frame):
    pass

img = cv.imread("gambar/original_image.jpg", cv.COLOR_RGB2HSV)

ap = argparse.ArgumentParser()
ap.add_argument("-c", "--camera", type=int, default=0, help="change camera")
ap.add_argument("-d", "--display", type=int, default=1, help="Whether or not frame should be displayed")
args = ap.parse_args()



cap = WebcamVideoStream(0).start()

while True:
    frame = cap.read()
    #frame = cv.imread("gambar/original_image.jpg", cv.COLOR_RGB2HSV)
    frame =  imutils.resize(frame, width=300)
    tinggi, panjang, _ = frame.shape
    filtered = color_filter(frame)

    if args.display > 0:
        #cv.imshow("result", result)
        #cv.imshow("mask", mask)
        cv.imshow("frame", filtered)

    key = cv.waitKey(1)
    if key == 27:
        break

cap.stop()
cv.destroyAllWindows()
