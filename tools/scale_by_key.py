import cv2
import numpy as np

cv2.namedWindow('image')
cv2.namedWindow('Control Window')


print " Zoom In-Out demo "
print " Press u to zoom "
print " Press d to zoom "

img = cv2.imread('../data/logo.png')


while(1):
    h,w = img.shape[:2]

    cv2.imshow('image',img)
    k = cv2.waitKey(10)

    if k==27 :
        break

    elif k == ord('u'):  # Zoom in, make image double size
        img = cv2.pyrUp(img,dstsize = (2*w,2*h))

    elif k == ord('d'):  # Zoom down, make image half the size
        img = cv2.pyrDown(img,dstsize = (w/2,h/2))
    print '------>'

cv2.destroyAllWindows()
