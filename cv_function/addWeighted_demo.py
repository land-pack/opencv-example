import cv2
import numpy as np

img1 = cv2.imread('../data/apple.png')
img2 = cv2.imread('../data/logo.png')

img11 = img1[0:50, 0:50]
img22 = img2[0:50, 0:50]


img3 = cv2.addWeighted(img11, 0.6, img22, 0.4, 0) 
img4 = cv2.addWeighted(img11, 0.8, img22, 0.2, 0) 

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('img3', img3)
cv2.imshow('img4', img4)

cv2.waitKey(0)
cv2.destroyAllWindows()
