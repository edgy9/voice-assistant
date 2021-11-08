import numpy as np
import cv2

img = cv2.imread('messi5.jpg')
kernal = np.ones((5,5),np.uint8)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7,7), 0)
imgCanny = cv2.Canny(img, 150, 200)
imgDialation = cv2.dilate(imgCanny, kernal,iterations=1)
imgEroded = cv2.erode(imgDialation, kernal, iterations=1)
cv2.imshow('image', imgGray)
cv2.imshow('imageblur', imgBlur)
cv2.imshow('imagecanny', imgCanny)
cv2.imshow('imagedialation', imgDialation)
cv2.imshow('imagederodedtion', imgEroded)


cv2.waitKey(0)