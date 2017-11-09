import numpy as np
import cv2


# Load a image from locate path


img = cv2.imread("apple.png", 0)

cv2.imwrite("apple_copy.png", img)

