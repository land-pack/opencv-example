import numpy as np
import cv2

# Load an color image in graysscale

img = cv2.imread("apple.png")

cv2.imshow('image', img)
cv2.waitKey()
cv2.destroyAllWindows()
