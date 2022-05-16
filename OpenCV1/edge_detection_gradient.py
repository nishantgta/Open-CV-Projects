#gradients and edges are different things
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("Putin.jpg")
cv.imshow("Original Image",img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#LAPLACIAN
#looks like a pencil shading of image
#when you transition from black to white or white to black,that's considered a +ve and -ve slope
#images itself cannot have -ve pixel values, hence all pixel values of the image are converted #to absolute values 
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow("Laplacian",lap)

#Sobel
#calculates gradients in two directions, X and Y
sobelx = cv.Sobel(gray, cv.CV_64F, 1 ,0) #X->1, Y->0
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1) #X->0, Y->1

""" cv.imshow("Sobel X", sobelx)
cv.imshow("Sobel Y", sobely) """

#combine both sobel images
combine_sobel= cv.bitwise_or(sobelx,sobely)
cv.imshow("Combined Sobel",combine_sobel)

#canny edges
canny = cv.Canny(gray,150,175)
cv.imshow("Canny Edges",canny)
#canny uses sobel in one of its stages

cv.waitKey(0)