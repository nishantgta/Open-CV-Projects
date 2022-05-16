import cv2
from random import randrange
trained_face_data=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#to capture video from webcam
#0 to wo webcam hi khol dega
webcam=cv2.VideoCapture('Wow.mp4')   #video doge to uska use karenge

#iterate over all frames
while True:
    successful_frame_read, frame=webcam.read() #first thing is whether reading the frame is successful or not.frame stores the actual image that is being read currently
    grayscaled_img=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    face_coordinates=trained_face_data.detectMultiScale(grayscaled_img)
    for (x,y,w,h) in face_coordinates:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(randrange(256),randrange(256),randrange(256)),2)
    cv2.imshow("Yo",frame)
    key=cv2.waitKey(1)                          #waitkey mein 1000 hone se wo har 1 sec pe frame show karega, agar kuch nhi hoga to key press karne pe current frame show hoga                   
    
    #stop if Q is pressed, 81 and 113 are ASCII value for Q and q respectively
    if key==81 or key==113:
        break

#release the memory in webcam object
webcam.release()
