#shifting an image along X and Y axis
import cv2 as cv
import numpy as np

img = cv.imread("/home/nishant/Documents/opencv/presspack20.0.jpg")

def translation(img, x, y): #x=shift by x pixels, y=shift by y pixels
    #-ve x=shift left
    #+ve y=shift down
    #+ve x=shift right
    #-ve y=shift up
    translation_matrix = np.float32([[1,0,x],[0,1,y]])
    dimension = (img.shape[1],img.shape[0]) #1 for width , 0 for height
    translated_matrix = cv.warpAffine(img, translation_matrix,dimension)
    return translated_matrix

img_after_translation = translation(img,100,100)
cv.imshow("Image after translation",img_after_translation)

img_after_translation = translation(img,-100,-100)
cv.imshow("Image after translation 1",img_after_translation)

#Rotation, rotate an image by some angle
#you can rotate around any point, choosing that point as origin
def rotation(img, angle, ref_point=None):
    height = img.shape[0] #height,width=img.shape[:2]
    width = img.shape[1]

    if ref_point is None: #them rotate around the center of the image
        ref_point = (width//2,height//2)

    #create a rotation matrix(like what we created in translation matrix)
    rotation_matrix = cv.getRotationMatrix2D(ref_point,angle,1.0) #reference point and angle through which we will rotate
    dimensions = (width,height)

    rotated_matrix = cv.warpAffine(img,rotation_matrix,dimensions)
    return rotated_matrix

img_after_rotation = rotation(img,45) #specify negative values for clockwise

cv.imshow("Image after Rotation", img_after_rotation)

#Resizing an image
resize1 = cv.resize(img, (500,500),interpolation=cv.INTER_AREA)
resize2 = cv.resize(img, (500,500),interpolation=cv.INTER_CUBIC)
resize3 = cv.resize(img, (500,500),interpolation=cv.INTER_LINEAR)
cv.imshow("Resize Area", resize1)
cv.imshow("Resize Cubic",resize2)
cv.imshow("Resize Linear",resize3)
#shrinking=INTER_AREA
#enlarging=INTER_LINEAR or INTER_CUBIC

#flipping,you don't need to create a function
#flip code can either be 0,1,-1 
#0-> flipping the image vertically
#1-> flipping the image horizontally
#-1-> flipping the image vertically or horizontally
flipped_image = cv.flip(img,0)
cv.imshow("Flipped Vertically",flipped_image)

flipped_image = cv.flip(img,1)
cv.imshow("Flipped Horizontally",flipped_image)

flipped_image = cv.flip(img,-1)
cv.imshow("Flipped Both",flipped_image)

#Cropping
crop = img[200:300,300:400]
cv.imshow("Cropped image",crop)

cv.waitKey(0)