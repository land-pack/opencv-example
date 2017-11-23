import cv2
import numpy as np


cv2.namedWindow('smooth')
cv2.namedWindow('smoothBar')

img1 = cv2.imread('../data/cck.png')
img2 = cv2.imread('../data/apple.png')

img11 = img1[ 20:100, 20:100]
img22 = img2[ 20:100, 20:100]

img3 = cv2.addWeighted(img11, float(5/10), img22, 0.5, 0)


#cv2.imshow('img1', img11)
#cv2.imshow('img2', img22)
#cv2.imshow('img3', img3)

def nothing(x):
    pass

cv2.createTrackbar('mybar', 'smoothBar', 0, 100, nothing)


while (1):
    cv2.imshow('smooth', img3)
    scale = cv2.getTrackbarPos('mybar', 'smoothBar')
    #scale = scale if scale > 0 else 1
    print 'scale --', scale
    i = float(scale) / 100.0
    print 'i----->', i
    #img3 = cv2.addWeighted(img11, float(i/100), img22, float(scale/100), 0)
    img3 = cv2.addWeighted(img11, i , img22, 1 - i, 0)


    k = cv2.waitKey(27)
    if k == ord('q'):
        break

cv2.destroyAllWindows()

