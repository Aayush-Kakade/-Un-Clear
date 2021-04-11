import cv2
import numpy as np

img = cv2.VideoCapture(0)

while(1):
    ret, frame = img.read()

    img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    img_invert = cv2.bitwise_not(img_gray)
    img_smooth = cv2.GaussianBlur(img_invert, (21,21),0)
    def finalsketch(x,y):
        return cv2.divide(x,255-y, scale=256)

    output = finalsketch(img_gray, img_smooth)
    cv2.imshow("Final Feed",output)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release
cv2.destroyAllWindows()
