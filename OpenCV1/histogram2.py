#compute a color histogram for a RGB image
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("/home/nishant/Documents/opencv/Putin.jpg")
cv.imshow("Original Image",img)

blank_img = np.zeros(img.shape[:2],dtype="uint8")

rec = cv.rectangle(blank_img,(81,53),(591,593),255,-1)
masked_color_putin = cv.bitwise_and(img,img,mask=rec)

cv.imshow("Color Putin Face",masked_color_putin)

colors = ('b','g','r') #tuple of colors

plt.figure()
plt.title("Coloured Histogram")
plt.xlabel("Bins")
plt.ylabel("Number of pixels")

col_channels = []
col_color = []

for i, column in enumerate(colors):
    #enumerate(colors)=0->'b',1->'g',2->'r'
    hist = cv.calcHist([img],[i],None,[256],[0,256])
    plt.plot(hist,color=column)
    plt.xlim([0,256])
    col_channels.append(i)
    col_color.append(column)
plt.show()

print (col_channels) #col_channels = 0,1,2(values of i in the loop)
print (col_color)

cv.waitKey(0)