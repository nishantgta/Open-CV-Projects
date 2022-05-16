import cv2
import mediapipe as mp
import time

mpDraw = mp.solutions.drawing_utils

mpPose = mp.solutions.pose
pose = mpPose.Pose()  #at false it will use detection and then tracking

cap = cv2.VideoCapture("taki.mp4")

ptime=0

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)

    print(results.pose_world_landmarks)

    if results.pose_world_landmarks:
          mpDraw.draw_landmarks(img, results.pose_world_landmarks, mpPose.POSE_CONNECTIONS)


    ctime = time.time()
    fps= 1/(ctime-ptime)
    ptime=ctime

    cv2.putText(img, str(int(fps)),(70,50),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)