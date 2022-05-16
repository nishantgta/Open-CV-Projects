import cv2

#our image which we have to check
img_file='highway.jpg'

#our pre trained car classifier
classifier_file='cars.xml'

#import the image
img=cv2.imread(img_file)

#convert image to black and white
black_n_white=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#create classifier,classifier classifies something as a pedestrian or cars
car_tracker=cv2.CascadeClassifier(classifier_file)

#detect cars
cars=car_tracker.detectMultiScale(black_n_white)

print(cars)

for x,y,w,h in cars:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

#display the images
cv2.imshow('Clever Programmer Image Detector',img)
cv2.waitKey()

print("Faguni")