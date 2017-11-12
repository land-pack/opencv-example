import numpy as np
import cv2

img = cv2.imread("../data/apple.png")

e1 = cv2.getTickCount()
for i in xrange(5, 49, 2):
	img = cv2.medianBlur(img, i)

e2 = cv2.getTickCount()

t = (e1 - e2) / cv2.getTickFrequency()

print t

# Default Optimization in OpenCV
# Check if optimization is enabled

print cv2.useOptimized()

