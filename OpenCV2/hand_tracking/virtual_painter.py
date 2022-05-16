import cv2
import numpy as np
import time
import mediapipe as mp
import os
import hand_tracking_module as htm

brushThickness =15
eraser_thickness = 50

folder_path = "Header"
mylist = os.listdir(folder_path)
overlay=[] #this will have all the images that we want to overlay
#print(mylist)

for im_path in mylist:
    image = cv2.imread(f'{folder_path}/{im_path}')
    overlay.append(image)

#print(len(overlay)) to check whether we have imported all the images
header = overlay[0] #initial value is here

draw_color = (255,0,255)

cap = cv2.VideoCapture(0)

cap.set(3,1280)
cap.set(4,720)
img_canvas = np.zeros((720,1280,3), np.uint8)  #new image will be made of the canvas, we are using numpy to draw our campus

detector = htm.handDetector(detectionCon=0.7)

xp,yp = (0,0)

while True:
     success, img = cap.read()  #import image
     img = cv2.flip(img, 1) #it will move in the same direction as your hand(easier to draw)

     #find hand landmarks
     img = detector.findHands(img)
     lm_list = detector.findPosition(img,draw=False)

     if len(lm_list)!=0:
         #print(lm_list)

         # tip of index finger
         x1, y1 = lm_list[8][1:] #unpacking here

         x2, y2 = lm_list[12][1:]  #unpacking

         #checking which fingers up(we want to draw when only one finger is up, and draw when only two fingers are up
         fingers = detector.fingers_up()
         #print(fingers)

         #if selection mode(when two fingers are up)
         if fingers[1] and fingers[2]:
             xp, yp = 0, 0  # it is drawing a straight line whenever we have a selection
             print("Selection Mode")
             if y1<125:    #it means you are in header, checking for the click
                 if 250 < x1 < 450:
                     header = overlay[0]
                     draw_color = (255, 0, 255)

                 elif 550 < x1 < 750:
                     header = overlay[1]
                     draw_color = (255, 0, 0)

                 elif 800 < x1 < 950:
                     header = overlay[2]
                     draw_color = (0, 255, 0)

                 elif 1100 < x1 < 1250:
                     header = overlay[3]
                     draw_color = (0, 0, 0)

             cv2.rectangle(img, (x1, y1 - 25), (x2, y2 + 25), draw_color, cv2.FILLED)

         #if drawing mode-Index finger is up
         if fingers[1] and fingers[2]==False:

             cv2.circle(img, (x1, y1), 15, draw_color, cv2.FILLED)
             print("Drawing Mode")

             if xp==0 and yp==0:  #if not this, then it will take from (0,0) to the starting point of the first frame
                 xp,yp = x1,y1

             if draw_color==(0,0,0):
                 cv2.line(img, (xp, yp), (x1, y1), draw_color, eraser_thickness)
                 cv2.line(img_canvas, (xp, yp), (x1, y1), draw_color, eraser_thickness)
             else:
                 cv2.line(img, (xp, yp), (x1, y1), draw_color, brushThickness)
                 cv2.line(img_canvas, (xp, yp), (x1, y1), draw_color, brushThickness)

             xp, yp = x1, y1

     img_gray = cv2.cvtColor(img_canvas, cv2.COLOR_BGR2GRAY)
     _, img_inv = cv2.threshold(img_gray, 50, 255, cv2.THRESH_BINARY_INV) #black to white and white to black in our canvas
     img_inv = cv2.cvtColor(img_inv, cv2.COLOR_GRAY2BGR)
     img = cv2.bitwise_and(img, img_inv) #with and we are adding image inverse and the image(intersection)
     img = cv2.bitwise_or(img, img_canvas) #here you will use an or operation

     img[0:125, 0:1280] = header #setting the header image
     #img = cv2.addWeighted(img, 0.5, img_canvas,0.5,0) #will blend both canvas and the original image
     cv2.imshow("Image",img)
     #cv2.imshow("Canvas", img_canvas)
     cv2.waitKey(1)

