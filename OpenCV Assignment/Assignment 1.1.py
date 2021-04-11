import cv2
img = cv2.imread('Desktop\OpenCV Assignment\sampleimg.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
(thresh, img_BnW) = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)
cv2.imshow("Orignal Image",img)
cv2.imshow("Grayscale Image",img_gray)
cv2.imshow("Black n White Image",img_BnW)
cv2.waitKey(0)