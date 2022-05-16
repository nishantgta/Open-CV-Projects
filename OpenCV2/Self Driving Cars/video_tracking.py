import cv2
vid_file="New York.mp4"

classifier_file="cars.xml"
pedestrian="haarcascade_fullbody.xml"

video=cv2.VideoCapture(vid_file)

car_tracker=cv2.CascadeClassifier(classifier_file)
pedestrian_tracker=cv2.CascadeClassifier(pedestrian)
while True:
    (successful_read,frame)=video.read()

    #if block to prevent error on last frame
    if successful_read:
        grayscaled_img=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    else:
        break
    
    #get coordnates for cars and pedestrians
    car_coordinates=car_tracker.detectMultiScale(grayscaled_img)
    ped_coordinates=pedestrian_tracker.detectMultiScale(grayscaled_img)

    #draw rectangles for cars
    for x,y,w,h in car_coordinates:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
        cv2.rectangle(frame,(x+2,y+2),(x+w,y+h),(255,0,0),2)

    #drwa rectangles for pedestrians
    for x,y,w,h in ped_coordinates:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

    cv2.imshow("Faguni",frame)
    key=cv2.waitKey(1)

    if key==81 or key==113:
        break

video.release()
