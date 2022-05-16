#masking allows us to focus on certain parts of the image
#you can focus on faces in a photo consisting of people
import cv2 as cv
import numpy as np


img = cv.imread("/home/nishant/Documents/opencv/presspack20.0.jpg")
cv.imshow("original",img)

blank_img = np.zeros(img.shape[:2],dtype='uint8')
cv.imshow("Blank image",blank_img)

maske = cv.circle(blank_img,(img.shape[1]//2,img.shape[0]//2),100,255,-1) #circle on a blank image
#now you can change this mask to anywhere in the image
cv.imshow("Mask image",maske)

rectangle_mask = cv.rectangle(blank_img,(0,0),(img.shape[1]//2,img.shape[0]//2),255,-1)
cv.imshow("rectangle",rectangle_mask)

#circle and rectangle both are added in the mask
masked_image_circle = cv.bitwise_and(img,img,mask=maske)
cv.imshow("Mask Image 1",masked_image_circle) 

masked_image_rectangle = cv.bitwise_and(img,img,mask=rectangle_mask)
cv.imshow("Mask Image 2",masked_image_rectangle)

cv.waitKey(0)

#similarly you can create your own mask, by superimposing various shapes on blank image and using it as a mask
#note that mask should be of same size as that of the image