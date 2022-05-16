import cv2
import mediapipe as mp
import time

cap=cv2.VideoCapture(0)

mpHands = mp.solutions.hands  #a formality you have to do
hands = mpHands.Hands()  #static part False: means some time it will detect and other time it will track,all default values are given
mpDraw = mp.solutions.drawing_utils  #this is used to draw those 21 points(landmarks) and connect lines between them

ptime=0
ctime=0

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)  #convert form RGB to BGR because hands object use RGB
    results = hands.process(imgRGB)   #process the image and coverts it

    #print(results.multi_hand_landmarks) #we need to know when hand is detected or not
                                        #as soon as you get hand in webcam, it will detect and print coordinates

    #for extracting multiple hands, we use a for loop
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:  #for all hand landmarks in a frame
            for id, lm in enumerate(handLms.landmark): #id is for index number we will get the information of the hand,id numbers,index numbers
               #print(id,lm)   #at first you will get in decimal values, ratio of the image
               h,w,c=img.shape
               cx,cy = int(lm.x*w), int(lm.y*h)  #center coordinates of the hand, integer value we want in last
               print(cx,cy)
               if id==4:
                   cv2.circle(img,(cx,cy),15,(255,0,255),cv2.FILLED)

            mpDraw.draw_landmarks(img , handLms, mpHands.HAND_CONNECTIONS) #handLms is for a single hand
                                                                           #HAND_CONNECTIONS is to draw lines btw. points

    ctime=time.time() #this will give us the current time
    fps=1/(ctime-ptime)  #frequency is calculated vro
    ptime=ctime

    cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),3) #first 3 is scale, second 3 is thickness

    cv2.imshow("Image" , img)
    cv2.waitKey ( 1 )