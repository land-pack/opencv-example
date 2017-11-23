import cv2
import numpy as np

img = cv2.imread('../data/logo.png')

cv2.namedWindow('scaleFactor')
cv2.namedWindow('image')

def nothing(x):
    print 'x--->', x

cv2.createTrackbar('scale','scaleFactor', 0 , 5, nothing)

rows, cols = img.shape[:2]

while(1):

    cv2.imshow('image', img)
    scaleFactor = cv2.getTrackbarPos('scale','scaleFactor') or 1
    scaleFactor = scaleFactor if scaleFactor > 0 else 1
    img = cv2.resize(img, (int(rows * scaleFactor), int(cols * scaleFactor)), interpolation=cv2.INTER_LINEAR)


    k =cv2.waitKey(10)
    if k == 27:
        break
    print 'scaleFactor -->', scaleFactor 

cv2.destroyAllWindows()
