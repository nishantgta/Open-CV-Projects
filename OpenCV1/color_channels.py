#how to split and merge color channels in open cv
#BGR- Red+Green+Blue merged together(opencv allows to split the image into these channels)
import cv2 as cv
import numpy as np

img = cv.imread("/home/nishant/Documents/opencv/presspack20.0.jpg")
cv.imshow("Original Image",img)

b,g,r = cv.split(img)

#all three are depicted as displayed as gray scale images
#shows the distribution of pixel intensity
#brighter region shows there is a greater concentration of corresponding color in thar region
#number of color channels in b,g,r is 1
#original image has three color channels
cv.imshow("Blue",b)
cv.imshow("Green",g)
cv.imshow("Red",r)

merge_image = cv.merge([b,g,r])
cv.imshow("Merged Image",merge_image) #you merged three color channels, to get original image

cv.waitKey(0)