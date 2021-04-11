import cv2
import numpy as np

img = cv2.imread("Desktop\OpenCV Assignment\sampleimg.jpg")

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img_invert = cv2.bitwise_not(img_gray)

img_smooth = cv2.GaussianBlur(img_invert, (21,21), sigmaX=0, sigmaY=0)

def dodgeV2(x,y):
    return cv2.divide(x,255-y, scale=256)

image_fn = dodgeV2(img_gray, img_smooth)
cv2.imshow('final',image_fn)

cv2.waitKey(0)