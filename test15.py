import cv2
import numpy as mp

img = cv2.imread('messi5.jpg')
print(img.shape)

imgResize = cv2.resize(img,(1000,500))


imgCropped = img[0:200,200:500]

cv2.imshow('image',img)
cv2.imshow('imageresize',imgResize)
cv2.imshow('imagerecrop',imgCropped)
cv2.waitKey(0)