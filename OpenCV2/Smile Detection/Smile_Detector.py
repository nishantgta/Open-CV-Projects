import cv2

face_detector=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
smile_detector=cv2.CascadeClassifier("haarcascade_smile.xml")
eye_detector=cv2.CascadeClassifier("haarcascade_eye.xml")

webcam=cv2.VideoCapture(0)

while True:
    successful_frame_read, frame=webcam.read()

    if not successful_frame_read:
        break

    frame_grayscale=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    faces=face_detector.detectMultiScale(frame_grayscale)  #detect all the faces in the images
    
    for x,y,w,h in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

        #get the sub frame using numpy(Nth dimensional slicing)
        the_face=frame[y:y+h,x:x+w]  #you are not making a copy here

        #change face to grayscale
        face_grayscale=cv2.cvtColor(the_face,cv2.COLOR_BGR2GRAY)

        #you are running smile on the face only
        smiles=smile_detector.detectMultiScale(face_grayscale,scaleFactor=1.7,minNeighbors=20)
        #scaleFactor is used to blurr the images,so as to reduce 
        #chance of detecting false positives

        eyes=eye_detector.detectMultiScale(face_grayscale,scaleFactor=1.3,minNeighbors=10)

        #find all smiles in the face
        for (X,Y,W,H) in smiles:
            #draw rectangles around that smile
            cv2.rectangle(the_face,(X,Y),(X+W,Y+W),(255,0,0),2)   #coordinates tune the_face se uthaye hain aur bna tu frame mein rha hain

        for x1,y1,w1,h1 in eyes:
            cv2.rectangle(the_face,(x1,y1),(x1+w1,y1+h1),(125,125,125),3)

        if len(smiles)>0:
            cv2.putText(frame,'Smiling',(x,y+h+40),fontScale=3,fontFace=cv2.FONT_HERSHEY_PLAIN,color=(255,255,255))

    cv2.imshow("Nishant",frame)
    key=cv2.waitKey(1)

    if key==81 or key==113:
        break

webcam.release()
cv2.destroyAllWindows()