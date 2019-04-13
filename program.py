import rw_file as rw
import cv2 as cv
import imutils


l_h_gawang = int(rw.read("setting/LH_gawang.txt"))
l_s_gawang = int(rw.read("setting/LS_gawang.txt"))
l_v_gawang = int(rw.read("setting/LV_gawang.txt"))
u_h_gawang = int(rw.read("setting/UH_gawang.txt"))
u_s_gawang = int(rw.read("setting/US_gawang.txt"))
u_v_gawang = int(rw.read("setting/UV_gawang.txt"))
dilation_gawang= int(rw.read("setting/dilation_gawang.txt"))
dilation_iterations = int(rw.read("setting/dilation_iteration_gawang.txt"))
erosion_gawang = int(rw.read("setting/erosion_gawang.txt"))
erosion_iterations = int(rw.read("setting/erosion_iteration_gawang.txt"))
gaussian_gawang = int(rw.read("setting/gaussian_gawang.txt"))
radius_gawang = int(rw.read("setting/radius_gawang.txt"))

l_h_bola = int(rw.read("setting/LH.txt"))
l_s_bola = int(rw.read("setting/LS.txt"))
l_v_bola = int(rw.read("setting/LV.txt"))
u_h_bola = int(rw.read("setting/UH.txt"))
u_s_bola = int(rw.read("setting/US.txt"))
u_v_bola = int(rw.read("setting/UV.txt"))
dilation_bola= int(rw.read("setting/dilation_bola.txt"))
dilation_iteration_bola = int(rw.read("setting/dilation_iteration_bola.txt"))
erosion_bola = int(rw.read("setting/erosion_bola.txt"))
erosion_iteration_bola = int(rw.read("setting/erosion_iteration_bola.txt"))
gaussian_bola = int(rw.read("setting/gaussian_bola.txt"))
radius_bola = int(rw.read("setting/radius_bola.txt"))


def detectObject(frame,lh,ls,lv,uh,us,uv,dilation,dil_iter,erosion,eros_iter,gaussian,radius):

    if gau

cap = cv.VideoCapture(0)
cap.set(cv.CAP_PROP_FRAME_WIDTH, 120)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, 240)

def main():
    while True:
        _, frame = cap.read()
        frame = imutils.resize(frame, width=300)
        tinggi, panjang = frame.shape