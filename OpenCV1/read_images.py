#how to read images and videos in opencv 
import cv2 as cv
img = cv.imread('/home/nishant/Documents/opencv/Putin.jpg') #this method takes path to an image and return that image as a matrix of pixels

cv.imshow("Logo", img) #displays the image as a new window, takes two parameters, the name of the window, and the actual matrix of the pixels

cv.waitKey(0) #it waits for a give amount of time for the key to be pressed