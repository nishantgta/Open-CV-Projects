import math
import pycaw
import cv2
import numpy as np
import time
import hand_tracking_module as htm
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


##############################
wcam, hcam= 640, 488
##############################

cap = cv2.VideoCapture(0)   #you changed the specification
cap.set(3, wcam)
cap.set(4, hcam)

ptime = 0

detector = htm.handDetector(detectionCon=0.7)

#it seems like initialisation, we will not change it
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
#volume.GetMute()
#volume.GetMasterVolumeLevel()
vol_range = volume.GetVolumeRange()
#print(volume.GetVolumeRange())  #-65.25 to 0 is our range
minVol = vol_range[0]
maxVol = vol_range[1]
vol = 0
volbar = 400
volper=0

while True:
    success, img = cap.read()

    img = detector.findHands(img)
    lmlist = detector.findPosition(img, draw=False)  #will contain list of all landmarks for a single frame
    if len(lmlist)!=0:  #otherwise you will get error when you dont show hands, as the list then will be empty
      #print(lmlist[4],lmlist[8])  # 4 and 8 for tip of thumb and index

      x1, y1 = lmlist[4][1],lmlist[4][2] #first element as x and second element as y
      x2, y2 = lmlist[8][1],lmlist[8][2] #coordinates of the tip of the index finger
      cx, cy = (x1+x2)//2 , (y1 + y2)//2 #coordinates of center of the line segment joining (x1,y1) & (x2,y2)
                                         #with the help of length, we can change volume

      cv2.circle(img, (x1, y1), 10, (255, 0, 0), cv2.FILLED)
      cv2.circle(img, (x2, y2), 10, (255, 0, 0), cv2.FILLED)
      cv2.circle(img, (cx, cy), 10, (255, 0, 0), cv2.FILLED)
      cv2.line(img, (x1,y1), (x2,y2), (255,255,255), 3)

      length = math.hypot(x2-x1,y2-y1)
      #print(length)

      #hand range is from 5- to 300
      #volume range is from -65 to 0

      vol = np.interp(length,[50,300],[minVol,maxVol])
      volbar = np.interp(length, [50, 300], [400,150])
      volper = np.interp(length, [50,300], [0, 100])

      print(vol)
      volume.SetMasterVolumeLevel(vol, None)

      if length < 50:
          cv2.circle(img, (cx,cy), 10, (0,255,0), cv2.FILLED)

      cv2.rectangle(img, (50, 150), (85, 400), (0, 0, 255), 3)
      cv2.rectangle(img, (50,int(volbar)), (85, 400), (0, 0, 255),cv2.FILLED)
      cv2.putText(img, f'{int(volper)}', (40, 450), cv2.FONT_HERSHEY_COMPLEX,1 ,(0,250,0), 3)

    ctime = time.time()
    fps = 1/(ctime-ptime)
    ptime = ctime

    cv2.putText(img, f'FPS: {int(fps)}', (40,50), cv2.FONT_HERSHEY_COMPLEX,1 ,(255, 0, 0), 2)

    cv2.imshow("Image",img)
    cv2.waitKey(1)