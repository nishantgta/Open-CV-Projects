#resizing and rescaling are done to reduce the computational information of a image
import cv2 as cv
img = cv.imread("/home/nishant/Documents/opencv/Rockstar_Games_Logo.svg.png")
cv.imshow('Yo',img)

capture = cv.VideoCapture(0)

def changeRes(height,width):
    #this works only for live video, it will not work for standalone files
    capture.set(3,height)
    capture.set(4,height)


#to rescale the frame
def rescaleFrame(frame, scale=0.75):
    dim = frame.shape
    print(dim)
    width = int(dim[1] * scale) #frame.shape will return the width of an image
    height = int(dim[0] * scale) #frame.height will return the height of an image
    dimension = (width,height) #a tuple of dimensions

    return cv.resize(frame, dimension,interpolation=cv.INTER_AREA) #resizes an image to a particular dimension

img = cv.imread("/home/nishant/Documents/opencv/Rockstar_Games_Logo.svg.png")
resized_image = rescaleFrame(img)
cv.imshow('Bhai',resized_image)

while True:
    isread, frame = capture.read() 
    resized_frame = rescaleFrame(frame) 
    cv.imshow("Original",frame) 
    cv.imshow("Resized" , resized_frame) 

    if cv.waitKey(20) and 0xFF==ord('d'):
        break

capture.release() 
cv.destroyAllWindows() 