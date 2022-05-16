#another way of finding the contours
import cv2 as cv
import numpy as np
img = cv.imread("/home/nishant/Documents/opencv/presspack20.0.jpg")

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray",gray)

edge = cv.Canny(img,125,175)
cv.imshow("Edge",edge)

blank_img = np.zeros(img.shape,dtype="uint8")
cv.imshow("Blank",blank_img)

#use threshold method to find the contours
ret,thresh = cv.threshold(gray,125,255,cv.THRESH_BINARY)
cv.imshow("Thresh image",thresh)
#thresholding looks into an image and tries to binarise the image
#if intensity of a pixel is below 125, the pixel is set to black(0)
#if intensity of a pixel is above 255, the pixel is set to white(1)
#THRESH_BINARY as we are binarising the image

contour, heirarchies = cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)

print(f'{len(contour)} contours are found')

#draw the found contours on the blank image,to know what kind of contours opencv found
cv.drawContours(blank_img,contour,-1,(0,0,255),1) #-1 specify all the contours in the list
cv.imshow("Image contours",blank_img)

cv.waitKey(0)