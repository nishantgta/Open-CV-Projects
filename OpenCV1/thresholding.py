#thresholding is a binarization of an image
#we take an image and convert it into a binary image
#pixels are either 0(black) or 1(white)
#you can set a thresholding value, above it is white and below it becomes black
import cv2 as cv
import numpy as np

img = cv.imread("/home/nishant/Documents/opencv/Putin.jpg")
cv.imshow("Original Image",img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray version",gray)

#SIMPLE THRESHOLDING
thresholds,thresh = cv.threshold(gray, 150, 255,cv.THRESH_BINARY)
#150->thresholded value
#more than 150-> set it to 255
#THRESH_BINARY-> looks at the image, compares each pixel value to 150
#thresh->thresholded image(binarized image), thresholds=150
cv.imshow("Simple threshold",thresh)

#create inverse thresholded image
thresholds,thresh_inv = cv.threshold(gray,150,255,cv.THRESH_BINARY_INV)
cv.imshow("Simple threshold inverse",thresh_inv)

#ADAPTIVE thresholding
#in above cases, we have manually supplied a threshold value
#so we will let computer decide the optimal threshold value
adaptive_thresh = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,3)
#you have to supply the kernel size also
#C is an integer value that is subtracted from the mean
cv.imshow("Adaptive thresholding",adaptive_thresh)

cv.waitKey(0)