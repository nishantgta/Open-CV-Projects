import cv2 as cv
import numpy as np

img = cv.imread("/home/nishant/Documents/opencv/presspack20.0.jpg")
cv.imshow("Original Image",img)

blank_img = np.zeros(img.shape[:2],dtype="uint8")
cv.imshow("Blank Image",blank_img)

rectangle_mask = cv.rectangle(blank_img,(0,0),(img.shape[1]//2,img.shape[0]//2),255,-1)
cv.imshow("Rectngle Mask",rectangle_mask)

final = cv.bitwise_and(img,img,mask=rectangle_mask)
cv.imshow("Final Image",final)

cv.waitKey(0)