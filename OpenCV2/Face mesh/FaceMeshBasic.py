import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)

ptime=0

mpDraw = mp.solutions.drawing_utils
mpFaceMesh = mp.solutions.face_mesh
facemesh = mpFaceMesh.FaceMesh(max_num_faces=4)
#to change the specifications of the lines and circles on the faces
draw_spec = mpDraw.DrawingSpec(thickness=1, circle_radius=2)


while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = facemesh.process(imgRGB)

    if results.multi_face_landmarks:
        for facelms in results.multi_face_landmarks:
            mpDraw.draw_landmarks(img, facelms, mpFaceMesh.FACE_CONNECTIONS,draw_spec,draw_spec)

        for id,lm in enumerate(facelms.landmark):
            #print(lm)
            ih, iw, ic = img.shape
            x, y = int(lm.x*iw),int(lm.y*ih)
            print(id,x,y)

    ctime=time.time()
    fps=1/(ctime-ptime)
    ptime=ctime
    cv2.putText(img,f'fps: {int(fps)}',(20,70),cv2.FONT_HERSHEY_PLAIN,3,(0,255,0),3)

    cv2.imshow("Image",img)
    cv2.waitKey(1)