import cv2 as cv

#we smooth an image when it has a lot of noise
#suppose you have an image, you define a kernel window over the image,size of lets say 3X3
#blur is applied to the middle pixel, as result to the pixel around it

#Averaging->we define a kernel window over a specific portion of the image, the middle pixel's 
#           intensity is set to average of the surrounding pixels of that pixel
#this process happens across the image
 
img = cv.imread("/home/nishant/Documents/opencv/presspack20.0.jpg")

average = cv.blur(img, (3,3)) #blur uses the above average method
cv.imshow("Blurred image",average)

#instead of average of the pixel intensity, there is a weight associated, which gives the value for the pixel
gauss = cv.GaussianBlur(img, (3,3),0) #0->standard deviation along X axis
cv.imshow("Gaussian Blur",gauss)

#Median Blur->instead of finding average, we find the median
#It is better than average blur
median = cv.medianBlur(img,3) #kernel size will not be an integer of size 3X3,just an integer
cv.imshow("Median",median)

#Bilateral Blurring->most effective,used in advance computer vision
#it blurs the image, but retains the edges
bilateral = cv.bilateralFilter(img, 5,15,15)
#3rd is sigma color, larger value means more colors in the neighbourhood will be considered for blurring
#4th is sigma space, which specifies how many pixels further out will be considered or not
cv.imshow("Bilateral image",bilateral)
#when you will give large values, it will start to look like median blur

cv.waitKey(0)