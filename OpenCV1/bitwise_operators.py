import cv2 as cv
import numpy as np
#and,or,xnor,not
#used in masking

blank_img = np.zeros((400,400),dtype="uint8")
rectangle = cv.rectangle(blank_img.copy(),(30,30),(370,370),255,-1)
circle = cv.circle(blank_img.copy(),(200,200),200,255,-1)

cv.imshow("Rectangle",rectangle)
cv.imshow("Circle",circle)

#bitwise and
bit_and = cv.bitwise_and(rectangle,circle)
cv.imshow("Bitwise And",bit_and)

#bitwise or
bit_or = cv.bitwise_or(rectangle,circle)
cv.imshow("Bitwise or",bit_or)

#bitwise XOR
bit_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow("Bitwise xor",bit_xor)

#bitwise NOT
bit_not = cv.bitwise_not(rectangle)
cv.imshow("Bitwise NOT",bit_not)

cv.waitKey(0)