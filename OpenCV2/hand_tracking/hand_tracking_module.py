import cv2
import mediapipe as mp
import time

class handDetector():
    def __init__(self,mode=False,maxHands=4,detectionCon=0.5,trackCon=0.5):  #we will give our parameters, basic ones for hands
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpHands = mp.solutions.hands  # a formality you have to do
        self.hands = self.mpHands.Hands(self.mode,self.maxHands,self.detectionCon,self.trackCon)  # static part False: means some time it will detect and other time it will track,all default values are given
        self.mpDraw = mp.solutions.drawing_utils  # this is used to draw those 21 points(landmarks) and connect lines between them
        self.tip_ids=[4,8,12,16,20]

    def findHands(self,img,draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # convert form RGB to BGR because hands object use RGB
        self.results = self.hands.process(imgRGB)  # process the image and coverts it

        # print(results.multi_hand_landmarks) #we need to know when hand is detected or not
        # as soon as you get hand in webcam, it will detect and print coordinates

        # for extracting multiple hands, we use a for loop
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:  # for all hand landmarks in a frame
                if draw:
                   self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)  # handLms is for a single hand

        return img

    def findPosition(self,img,handNo=0,draw=True):  #we are giving the parameters of the image

        self.lmList=[]
        if self.results.multi_hand_landmarks:  #if results is not self, then you cannot use it in findPosition object
            myHand=self.results.multi_hand_landmarks[handNo]

            for id, lm in enumerate(myHand.landmark):  # id is for index number we will get the information of the hand,id numbers,index numbers
                # print(id,lm)   #at first you will get in decimal values, ratio of the image
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)  # center coordinates of the hand, integer value we want in last
                #print(id,cx, cy)
                self.lmList.append([id,cx,cy])
                #if id == 4:
                if draw:
                   cv2.circle(img, (cx, cy), 10, (255, 0, 255), cv2.FILLED)

        return self.lmList

    def fingers_up(self):
        fingers = []

        # thumb
        if self.lmList[self.tip_ids[0]][1] < self.lmList[self.tip_ids[0] - 1][1]:  # for thumb, we will check tip of thumb with lm just below it, along X-axis
            fingers.append(1)
        else:
            fingers.append(0)

        for id in range(1, 5):
            if self.lmList[self.tip_ids[id]][2] < self.lmList[self.tip_ids[id] - 2][2]:  # here we are checking tip with lm 2 points below it, along Y axis
                fingers.append(1)
            else:
                fingers.append(0)
        return fingers

def main():
    ptime = 0
    ctime = 0
    cap = cv2.VideoCapture(0)
    detector = handDetector()    #detector becomes an object of class handDetector
    while True:
        success, img = cap.read()
        img = detector.findHands(img)   #we have to give our image, nothing will be drawn if this false
        lmList = detector.findPosition(img)   #if we give here draw=False, then the dots will not be there
        if len(lmList)!=0:
           print(lmList[4])

        ctime = time.time()  # this will give us the current time
        fps = 1 / (ctime - ptime)  # frequency is calculated vro
        ptime = ctime

        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255),
                    3)  # first 3 is scale, second 3 is thickness

        cv2.imshow("Image", img)
        cv2.waitKey(1)



if __name__=="__main__":  #used to showcase what can this module do
    main()