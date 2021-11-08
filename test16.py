import cv2
import numpy as np
from numpy.lib.type_check import imag

def empty(a):
    pass

def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver






cv2.namedWindow('track bars')
cv2.resizeWindow('track bars', 640,340)
cv2.createTrackbar('hue min', 'track bars', 42, 179, empty)
cv2.createTrackbar('hue max', 'track bars', 54, 179, empty)
cv2.createTrackbar('sat min', 'track bars', 126, 255, empty)
cv2.createTrackbar('sat max', 'track bars', 226, 255, empty)
cv2.createTrackbar('val min', 'track bars', 112, 255, empty)
cv2.createTrackbar('val max', 'track bars', 178, 255, empty)




while True:
    img = cv2.imread('messi5.jpg')


    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("hue min",'track bars')
    h_max = cv2.getTrackbarPos("hue max",'track bars')
    s_min = cv2.getTrackbarPos("sat min",'track bars')
    s_max = cv2.getTrackbarPos("sat max",'track bars')
    v_min = cv2.getTrackbarPos("val min",'track bars')
    v_max = cv2.getTrackbarPos("val max",'track bars')
    print(h_min,h_max,s_min,s_max,v_min,v_max)
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = cv2.inRange(imgHSV,lower,upper)
    imgResult = cv2.bitwise_and(img,img,mask=mask)

    cv2.imshow('image', img)
    cv2.imshow('image', imgHSV)
    cv2.imshow('imask', mask)
    cv2.imshow('iask', imgResult)

    imgstack = stackImages(0.6,([img, imgHSV],[mask,imgResult]))
    cv2.imshow('stacked', imgstack)

    cv2.waitKey(1)