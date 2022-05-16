import cv2
import time
import os
import hand_tracking_module as htm

wcam, hcam = 800, 600

cap = cv2.VideoCapture(0)
cap.set(3, wcam) #3 is for width of cam
cap.set(4, hcam) #4 is for height of cam

#os is used for storing images
folder_path = "finger_images"
myList = os.listdir(folder_path)
#print(myList)

overlay_list = [] #because we want to overlay the images on our main image

for imPath in myList:
    image = cv2.imread(f'{folder_path}/{imPath}')
    overlay_list.append(image)

ptime = 0

detector = htm.handDetector(detectionCon = 0.75)

tip_ids=[4,8,12,16,20]

while True:
    success, img = cap.read()

    img = detector.findHands(img)
    lm_list = detector.findPosition(img, draw=False)

    if len(lm_list) != 0:
        fingers = []

        #thumb
        if lm_list[tip_ids[0]][1] > lm_list[tip_ids[0] - 1][1]:     #for thumb, we will check tip of thumb with lm just below it, along X-axis
            fingers.append(1)
        else:
            fingers.append(0)

        for id in range(1, 5):
           if lm_list[tip_ids[id]][2] < lm_list[tip_ids[id]-2][2]:  #here we are checking tip with lm 2 points below it, along Y axis
              fingers.append(1)
           else:
               fingers.append(0)

        total_fingers = fingers.count(1)
        print(total_fingers)
        #print(fingers)

        h, w, c = overlay_list[total_fingers-1].shape
        img[0:h, 0:w] = overlay_list[total_fingers-1]  # but we have to automate this
                                                       # when there are zero fingers, then the value of total_fingers-1 is -1, which will give overlay_list[-1]

        cv2.rectangle(img, (20, 225), (170, 425), (0,255,0), cv2.FILLED)
        cv2.putText(img, str(total_fingers), (45,375), cv2.FONT_HERSHEY_PLAIN, 10, (255,0,0), 25)

    ctime = time.time()
    fps = 1/(ctime-ptime)
    ptime = ctime
    cv2.putText(img, f'FPS:{int(fps)}', (400, 50), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)

    cv2.imshow("Image", img)
    cv2.waitKey(1)