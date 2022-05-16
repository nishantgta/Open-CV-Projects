import cv2
import mediapipe as mp
import time

cap=cv2.VideoCapture(0)
ptime=0

mpFaceDetection = mp.solutions.face_detection
mpDraw = mp.solutions.drawing_utils
facedetection = mpFaceDetection.FaceDetection(min_detection_confidence=0.75)  #so as to remove false positives

while True:
    success, img = cap.read()

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = facedetection.process(imgRGB)
    #print(results)

    if results.detections:
        for id,det in enumerate(results.detections):
            #mpDraw.draw_detection(img, det)
            # print(id, det)
            # print(det.score)  #print det and then see
            #print(det.location_data.relative_bounding_box)
            bboxc = det.location_data.relative_bounding_box
            ih, iw, ic = img.shape
            bbox = int(bboxc.xmin * iw), int(bboxc.ymin * ih), int(bboxc.width * iw), int(bboxc.height * ih)
            cv2.rectangle(img, bbox, (255,0,255), 3) #we are not using a default function(draw_detection), instead we are giving our own coordinates
            #you can print score, xmin, ymin, width, height

            cv2.putText(img, f'Score: {int(det.score[0]*100)}%', (bbox[0], bbox[1]-20), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)


    ctime = time.time()
    fps=1/(ctime-ptime)
    ptime=ctime
    cv2.putText(img,f'FPS: {int(fps)}',(20,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)