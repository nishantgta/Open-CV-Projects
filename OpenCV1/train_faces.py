#we will train our recognizer on the passed images
#we will use opencv built in library
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import os

haar_cascade = cv.CascadeClassifier("haar_face.xml")

people = []

for i in os.listdir("/home/nishant/Documents/opencv/People"):
    people.append(i) 

print(people)

dir = r"/home/nishant/Documents/opencv/People"

features = [] #image arrays of the faces
labels = [] #corresponding label, like whose face does it belong to

def create_train(): #this will essentially loop over every folder in our base folder, grab every image and add it to our training set
    for person in people:
        path = os.path.join(dir, person)
        cur_label = people.index(person)
        #now we are inside folder, then we are gonna loop inside the folder

        for img in os.listdir(path):
            img_path = os.path.join(path, img)

            image_array = cv.imread(img_path) #image array of the photo at given path
            gray_image = cv.cvtColor(image_array,cv.COLOR_BGR2GRAY) #coverted above photo into grayscale

            #now lets detect our faces
            faces = haar_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=4)

            for (x,y,w,h) in faces:
                faces_region_of_interest = gray_image[y:y+h,x:x+w] #cropped image of face pushed in the features 
                features.append(faces_region_of_interest)
                labels.append(cur_label) 
                #mapping between index and the image present in it, and not the string and the image, this will reduce strain 


create_train()

print("Training-------------------")

#we can use features and labels list now, to train our recognizers on it

#this is an instance of the given class
face_recognizer = cv.face.LBPHFaceRecognizer_create() #you have instantiated the face recognizer

features = np.array(features,dtype='object')
labels = np.array(labels)

#train the recognizer on features list and the labels list
face_recognizer.train(features,labels) #but before passing here, you have to convert them into numpy arrays

face_recognizer.save("training_faces.yml") #we can use trained faces in other directories

np.save('features.npy',features)
np.save('labels.npy',labels)

""" print(f'Length of the features={len(features)}')
print(f'Length of the Labels={len(labels)}') """




