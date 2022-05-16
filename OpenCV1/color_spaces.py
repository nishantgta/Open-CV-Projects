#ADVANCED CONCEPTS
#how to switch between color spaces in opencv
#a system of representing an array of pixel colors
#RGB, GRAYSCALE are color spaces 
import cv2 as cv
from cv2 import COLOR_HSV2BGR
import numpy as np

#matplot lib display RGB instead of BGR

img = cv.imread("/home/nishant/Documents/opencv/presspack20.0.jpg")
cv.imshow("Original Image",img) 

#BGR to GRAY
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray",gray)

#BGR to HSV(Hue Saturation Value)
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow("HSV image", hsv)

#BGR to LAB(l*a*b)
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow("LAB image", lab) #washed down version of the BGR image

#BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow("RGB image", rgb)

#HSV to BGR
hsvtobgr = cv.cvtColor(hsv,cv.COLOR_HSV2BGR)
cv.imshow("HSV to BGR",hsvtobgr)

cv.waitKey(0)