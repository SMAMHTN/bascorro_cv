import rw_file as rw
import cv2 as cv
import imutils
import numpy as np


l_h_gawang = int(rw.read("setting/LH_gawang.txt"))
l_s_gawang = int(rw.read("setting/LS_gawang.txt"))
l_v_gawang = int(rw.read("setting/LV_gawang.txt"))
u_h_gawang = int(rw.read("setting/UH_gawang.txt"))
u_s_gawang = int(rw.read("setting/US_gawang.txt"))
u_v_gawang = int(rw.read("setting/UV_gawang.txt"))

dilation_gawang= int(rw.read("setting/dilation_gawang.txt"))
dilation_iteration_gawang = int(rw.read("setting/dilation_iteration_gawang.txt"))
erosion_gawang = int(rw.read("setting/erosion_gawang.txt"))
erosion_iteration_gawang = int(rw.read("setting/erosion_iteration_gawang.txt"))
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


def detectObject(frame,tinggi,panjang,hsv,lh,ls,lv,uh,us,uv,dilation,dil_iter,erosion,eros_iter,gaussian,radius):


    lower = np.array([lh,ls,lv])
    upper = np.array([uh,us,uv])
    mask = cv.inRange(hsv, lower, upper)

    gaussian = rw.odd(gaussian)
    frame = cv.GaussianBlur(frame, (gaussian,gaussian),0)

    erosion = rw.odd(erosion)

    erosion_kernel = cv.getStructuringElement(cv.MORPH_RECT, (erosion,erosion))
    dilation_kernel = cv.getStructuringElement(cv.MORPH_RECT, (dilation,dilation))

    mask = cv.erode(mask, erosion_kernel, iterations= eros_iter)
    mask = cv.dilate(mask, dilation_kernel, iterations=dil_iter)

    result = cv.bitwise_and(frame, frame, mask= mask)

    contours, _ = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    x = 0
    y = 0
    center = None
    radius = None

    if len(contours) > 0:
        c = max(contours, key=cv.contourArea)
        ((x, y), radius) = cv.minEnclosingCircle(c)
        M = cv.moments(c)

        if int(M["m00"]) > 0:
            cx = int(M["m10"]) / int(M["m00"])
            cy = int(M["m01"]) / int(M["m00"])
            center = (int(cx), int(cy))

            rads = int(rw.read("setting/radius_gawang.txt"))
            if radius > rads :

                cv.circle(result, (int(x), int(y)), int(radius), (0,255,255), 2)
                cv.circle(result, center, 5, (0,0,255), -1)
                cv.putText(result, "x : {} y : {}".format(int(x), int(y)), (10, tinggi-25), cv.FONT_HERSHEY_COMPLEX_SMALL,0.8, (10,255,10))


    return result, mask, center, contours, x,y, radius


cap = cv.VideoCapture(0)
cap.set(cv.CAP_PROP_FRAME_WIDTH, 120)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, 240)

def main():
    while True:
        _, frame = cap.read()
        frame = imutils.resize(frame, width=300)
        tinggi, panjang, _  = frame.shape

        hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)

        result_gawang, mask_gawang, center_gawang, contours_gawang, x_gawang, y_gawang, rads_gawang = detectObject(frame,tinggi,panjang,hsv,l_h_gawang,l_s_gawang,l_v_gawang,u_h_gawang,u_s_gawang,u_v_gawang,dilation_gawang,dilation_iteration_gawang,erosion_gawang,erosion_iteration_gawang,gaussian_gawang,radius_gawang)

        if rads_gawang  != None and rads_gawang > radius_gawang:
            result_bola, mask_bola, center_bola, contours_bola, x_bola, y_bola, rads_bola = detectObject(
                frame, tinggi, panjang, hsv, l_h_bola, l_s_bola, l_v_bola, u_h_bola, u_s_bola, u_v_bola,
                dilation_bola, dilation_iteration_bola, erosion_bola, erosion_iteration_bola, gaussian_bola,
                radius_bola)
            print(x_bola,y_bola)


        else:
            # trigger function serial disini buat cari bola
            pass


        cv.imshow("frame", frame)
        cv.imshow("result_gawang", result_gawang)




        key = cv.waitKey(1)
        if key == 27:
            break

    cap.release()
    cv.destroyAllWindows()


if __name__ == "__main__":
    main()