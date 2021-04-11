import cv2
import numpy as np

img = cv2.imread("desktop\OpenCV Assignment\givenimg.png",0)

rows,cols = img.shape

M1 = np.float32([[1,0,80],[0,1,60]])
dst1 = cv2.warpAffine(img,M1,(cols,rows))

M2 = np.float32([[1,0,-70],[0,1,60]])
dst2 = cv2.warpAffine(img,M2,(cols,rows))

M3 = np.float32([[1,0,80],[0,1,-60]])
dst3 = cv2.warpAffine(img,M3,(cols,rows))

M4 = np.float32([[1,0,-80],[0,1,-60]])
dst4 = cv2.warpAffine(img,M4,(cols,rows))

cv2.imshow('Move Bottom Right',dst1)
cv2.imshow('Move Bottom Left',dst2)
cv2.imshow('Move Top Right',dst3)
cv2.imshow('Move Top Left',dst4)

M1 = cv2.getRotationMatrix2D((cols/2,rows/2),45,1)
dst1 = cv2.warpAffine(img,M1,(cols,rows))

M2 = cv2.getRotationMatrix2D((cols/2,rows/2),90,1)
dst2 = cv2.warpAffine(img,M2,(cols,rows))

M3 = cv2.getRotationMatrix2D((cols/2,rows/2),135,1)
dst3 = cv2.warpAffine(img,M3,(cols,rows))

M4 = cv2.getRotationMatrix2D((cols/2,rows/2),180,1)
dst4 = cv2.warpAffine(img,M4,(cols,rows))

cv2.imshow('Rotate 45',dst1)
cv2.imshow('Rotate 90',dst2)
cv2.imshow('Rotate 135',dst3)
cv2.imshow('Rotate 180',dst4)

blur1 = cv2.blur(img,(5,5))
blur2 = cv2.GaussianBlur(img,(5,5),0)

cv2.imshow('Simple Blur',blur1)
cv2.imshow('Guassian Blur',blur2)

cv2.waitKey(0)