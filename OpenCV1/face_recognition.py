import cv2 as cv
import numpy as np
import os

people = []

for i in os.listdir("/home/nishant/Documents/opencv/People"):
    people.append(i)

haar_cascade = cv.CascadeClassifier("haar_face.xml")

""" features = np.load("features.npy")
labels = np.load("labels.npy") """

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read("training_faces.yml")  #your trained model is stored here

img = cv.imread(r"/home/nishant/Documents/opencv/validation/putin_bhai_4.jpg")

gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Unidentified Person", gray_img)

#Detect the face in the image
face_rect = haar_cascade.detectMultiScale(gray_img, 1.1, 4)

for (x,y,w,h) in face_rect:
    region_of_interest = gray_img[y:y+h,x:x+w]

    label,confidence = face_recognizer.predict(region_of_interest)

    print(f"Label={people[label]} with a confidence of {confidence}")

    cv.putText(img,str(people[label]),(20,20),fontFace=cv.FONT_HERSHEY_COMPLEX,fontScale=1.0,color=(0,255,0),thickness=2)

    cv.rectangle(img, (x,y),(x+w,y+h),(255,0,0),2)

cv.imshow("Detected faces",img)

cv.waitKey(0)

