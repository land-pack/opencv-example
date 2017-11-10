import numpy as np
import cv2


# Create a  black image

d3 = np.zeros((4, 5, 3), np.uint8)
print d3
print '=' * 100
cv2.line(d3, (0,0),(4,4), (255, 0,0), 1)
print d3
cv2.imshow('frame', d3)

cv2.waitKey(0)
cv2.destroyAllWindows()
