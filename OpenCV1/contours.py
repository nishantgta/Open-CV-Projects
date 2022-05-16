#edges are determined by the change in the color intensity
#contours check for the continuous points having same color intensity
import cv2 as cv
import numpy as np

img = cv.imread("/home/nishant/Documents/opencv/presspack20.0.jpg")
cv.imshow("Original Image",img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray",gray)

blank_img = np.zeros(img.shape,dtype='uint8')

#blur the image before finding the edges and contours
blurred = cv.GaussianBlur(img,(5,5),cv.BORDER_DEFAULT)
cv.imshow("Blurred image",blurred)

edge = cv.Canny(blurred, 125,175)
cv.imshow("Image edge",edge)

contour, heirarchies = cv.findContours(edge,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE) #a mode in which to find the contours
#RETR_LIST to find all the contours in the image
#contour = python list of all the contours that are found in the image
#heirarchies = the heirarchical representaton of contours
#RETR_EXTERNAL returns only the external contours
#RETR_TREE returs all the heirarchical contours
#next parameter is contour approximation method
#CHAIN_APPROX_NONE: no approximation
#CHAIN_APPROX_SIMPLE: compresses all the contours that are returned into simple ones that makes sense, suppose you a line, C_A_N returns all the coordinates of the lines, C_A_S returns the two end points,
print(f'{len(contour)} contours are found')

cv.drawContours(blank_img,contour,-1,(0,0,255),1)
cv.imshow("Image contours",blank_img)

cv.waitKey(0)

#don't use threshold, because it is more simpler and doesn't do the job perfectly