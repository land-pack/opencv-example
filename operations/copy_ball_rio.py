import numpy as np
import cv2

img = cv2.imread("../data/roi.jpg")

print img

ball = img[180:140, 230:290]

print ball

#img[190:150, 240:300] = ball
img[:,:,2] = 0

cv2.imshow('image', img)

cv2.waitKey(0)

cv2.destroyAllWindows()
