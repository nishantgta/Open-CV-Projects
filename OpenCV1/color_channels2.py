import cv2 as cv
import numpy as np

img = cv.imread("/home/nishant/Documents/opencv/presspack20.0.jpg")
blank_img = np.zeros(img.shape[:2],dtype="uint8")

cv.imshow("Original",img)

cv.imshow("Blank",blank_img)

b,g,r = cv.split(img)
blue = cv.merge([b,blank_img,blank_img])
green = cv.merge([blank_img,g,blank_img])
red = cv.merge([blank_img,blank_img,r])

cv.imshow("Blue",blue)
cv.imshow("Green",green)
cv.imshow("Red",red)

cv.waitKey(0)