#they allow you to visualize pixel intensities
#a type of a graph or plot
#we can compute histograms for grayscale as well as RGB images
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("/home/nishant/Documents/opencv/Putin.jpg")
cv.imshow("Original Image",img)

blank_img = np.zeros(img.shape[:2],dtype="uint8")

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray",gray)

rec = cv.rectangle(blank_img,(81,53),(591,593),255,-1)

maske = cv.bitwise_and(gray,gray,mask=rec)
cv.imshow("Masked Putin",maske)

#GrayScale_Hist
gray_histogram = cv.calcHist([gray],[0],mask=maske,histSize=[256],ranges=[0,256])
#first parameter is the list of images
#histSize: number of bins we want to use when calculating our histogram
#ranges: the range of all possible pixel values

plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("Number of pixels")
plt.plot(gray_histogram)
plt.xlim([0,256])
plt.show()
#there are about 9200-9300 pixels that have an intensity of around 196 

#lets create an histogram on a mask
""" cv.imshow("Rectangle Mask",mask)
mask_putin = cv.bitwise_and(gray,gray,mask)

cv.imshow("Putin",mask_putin) """

cv.waitKey(0)