import cv2
from random import randrange
#to load some pre frontal data on face frontals from opencv
#classifier can classify something as face
trained_face_data=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#choose an image to detect faces
#imread ki madad se import karenge image ko
#image is like an array with bunch of numbers
img=cv2.imread('three.jpg')

#to convert to grayscale
grayscaled_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#to detect faces,no matter what the scale of the face is, smaller or big
face_coordinates=trained_face_data.detectMultiScale(grayscaled_img)
print(face_coordinates)

#draw rectangles
c=0
for x,y,w,h in face_coordinates:
   cv2.rectangle(img,(x,y),(x+w,y+h),(randrange(256),randrange(256),randrange(256)),5)
   c+=1
   if(c==3):
       break

#to show the imported image
cv2.imshow('Nishant bhai mahaan',img)

#waitkey nahi lgaoge to instantly close hoga
cv2.waitKey()

#print("Code Completed")