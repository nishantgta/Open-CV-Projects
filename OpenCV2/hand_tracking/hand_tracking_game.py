import cv2
import mediapipe as mp
import time
import hand_tracking_module as htm

ptime = 0
ctime = 0
cap = cv2.VideoCapture(0)
detector = htm.handDetector()    #detector becomes an object of class handDetector
while True:
        success, img = cap.read()
        img = detector.findHands(img)   #we have to give our image
        lmList = detector.findPosition(img)
        if len(lmList)!=0:
           print(lmList[4])

        ctime = time.time()  # this will give us the current time
        fps = 1 / (ctime - ptime)  # frequency is calculated vro
        ptime = ctime

        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255),
                    3)  # first 3 is scale, second 3 is thickness

        cv2.imshow("Image", img)
        cv2.waitKey(1)