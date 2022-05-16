import mediapipe as mp
import autopy
import cv2
import time
import numpy as np
import hand_tracking_module as htm

cap = cv2.VideoCapture(0)

wcam = 640
hcam = 480

cap.set(3, wcam)
cap.set(4, hcam)

ptime = 0

detector = htm.handDetector(maxHands=1)

while True:
    # 1. Find the hand landmarks
    success, img = cap.read()
    img = detector.findHands(img)
    lmlist = detector.findPosition(img)
    # 2. If only index finger, then hover mode else when both middle and index finger, then click mode
    # 3. Get the tip of the index and middle finger
    # 4. Check which fingers are up
    # 5. convert coordinates (webcam in 640*480 and screen in another resolution)
    # 6. smoothen values
    # 7. move mouse
    # 8. Both index and middle fingers are up, thne it is clicking mode
    # 9. Find distance between fingers
    #10. Click mouse if distance is short
    #11. Frame rate
    ctime = time.time()
    fps = 1/(ctime-ptime)
    ptime = ctime
    cv2.putText(img, str(int(fps)), (20,50), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,0), 3)

    #12 Display
    cv2.imshow("Image", img)
    cv2.waitKey(1)