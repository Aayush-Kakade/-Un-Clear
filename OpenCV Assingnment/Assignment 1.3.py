import cv2
import numpy as np

img = cv2.imread("Desktop\OpenCV Assignment\sampleimg.jpg")

output = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

cv2.imshow('org',img)
cv2.imshow('out',output)
cv2.waitKey(0)