import cv2 as cv
import numpy as np

img = cv.imread("selfie.jpg")
cv.imshow("Putin",img)

#haar cascade identifies a face by looking at the edges,it doesn't look for skin, mouth
gray_face = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray Putin",gray_face)

haar_cascade = cv.CascadeClassifier("haar_face.xml") #all thirty thousand lines of XML code are read and stored in the variable called haar_cascade. 

faces = haar_cascade.detectMultiScale(gray_face, scaleFactor=1.1, minNeighbors=6)
#the minimum number of neighbors a rectangle should have to be called a face
#detect a face and return its rectangular coordinates of that face as a list to faces_rect 
#we can loop over faces, and grab the coordinates and draw rectangles

print (f"Number of faces={len(faces)}")

for (x,y,w,h) in faces:
    cv.rectangle(img, (x,y),(x+w,y+h), (0,200,200),2)

cv.imshow("New Image",img)

cv.waitKey(0)