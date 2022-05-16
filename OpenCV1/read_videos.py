import cv2 as cv
capture = cv.VideoCapture("/home/nishant/Documents/opencv/yt1s.com - Why are You Running_480p.mp4")  #o,1,2,3 if you are using a webcam or a camera that is connected to your computer
#to read videos, we use a while loop and display the video frame by frame.

while True:
    isread, frame = capture.read() #this returns a frame,and a boolean that tells whether a frame is successfully read or not.
    cv.imshow("Your videos", frame)

    if cv.waitKey(20) and 0xFF==ord('d'): #to stop the video from playing indefinitely
        break                             #if letter 'd' is pressed, then break out of this loop
    #-215 assertion failed because opencv could not find a video at that point, video ran out of range
capture.release() 
cv.destroyAllWindows() 