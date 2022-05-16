#how to draw and write on images
import cv2 as cv
import numpy as np

#---drawing with the help of blank image---
blank_img = np.zeros((500,500,3),dtype='uint8') #height, width and number of color channels   
#you can also draw on your own image
blank_img2 = np.zeros((500,500,3),dtype='uint8')
blank_img3 = np.zeros((500,500,3),dtype='uint8')

#1. Paint the image a certain color
blank_img[:] = 0,255, 200  #: indicates over the entire image
cv.imshow("yo",blank_img)

blank_img2[200:300,300:500] = 255,255,255  #to color a particular region, from x[300,500], y[200,300]
cv.imshow("yo2",blank_img2) 

#2. Draw a rectangle
cv.rectangle(blank_img,(0,0),(250,250),(0,0,0),thickness=2)
cv.imshow("tera",blank_img)
#filling the rectangle
cv.rectangle(blank_img,(0,0),(250,250), (0,255,0),thickness=cv.FILLED) #in place of cv.FILLED you can use -1
cv.imshow("mera",blank_img)

#3. Draw a circle
cv.circle(blank_img3,(250,250),100,(255,255,255),thickness=4) #you can also fill this circle
cv.imshow("vro",blank_img3)

#4. Draw a line(takes two points as inputs and draws a line between them)
cv.line(blank_img3,(0,0),(250,250),(255,0,0),thickness=3)
cv.imshow("line",blank_img3)

#5. Write Text
cv.putText(blank_img,"Hello",(250,250),cv.FONT_HERSHEY_DUPLEX,1.0,(220,100,0),thickness=2)
cv.imshow("Font",blank_img)

#img = cv.imread("/home/nishant/Documents/opencv/Rockstar_Games_Logo.svg.png")
cv.waitKey(0)