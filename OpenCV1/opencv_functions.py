import cv2 as cv
img = cv.imread("/home/nishant/Documents/opencv/presspack20.0.jpg")
cv.imshow("Yo",img)   

#Converting an image to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) #convert a BGR image to GRAY
cv.imshow("yo2",gray) 

gmi = cv.cvtColor(img, cv.COLOR_BGR2RGB) #convert a BGR image to RGB
cv.imshow("yo2",gmi) 

#Blurring an image
blurred = cv.GaussianBlur(img, (5,5),cv.BORDER_DEFAULT) #this tuple should always be odd, kernel size
cv.imshow("Blur",blurred)

#Edge cascade(trying to find the edges which are present in the image)
#we will use the canny edge detector
edge = cv.Canny(img,125,175) #you can reduce the edges by essentially blurring the image
cv.imshow("Edges",edge)
edge_blur = cv.Canny(blurred,125,175)
cv.imshow("Blur Edges",edge_blur) 

#Dilate an image using specific structural elements, these are actually the edges
dilated = cv.dilate(edge_blur, (5,5),iterations=10) #dilate, in layman terms, will actually make your edges a little bit clearer 
cv.imshow("Dilated",dilated)

#Eroding
#you can get the structursl image back, with the help of eroding
eroded = cv.erode(dilated, (5,5),iterations = 10) 
cv.imshow("Eroding", eroded) 

#resizing an image
resize_img = cv.resize(img, (500,500),interpolation=cv.INTER_AREA)
#interpoltion is used when you are shrinking the image
#if you are enlarging the image, then you can use INTER_CUBIC, which is better than INTER_AREA and INTER_LINEAR
cv.imshow("Resized image", resize_img)

#CROPPING an image
#since image is bassically an array, you can use array slicing in python
cropped = img[50:200,100:300]
cv.imshow("Cropped Image",cropped)

cv.waitKey(0)