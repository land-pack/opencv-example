import cv2
import numpy as np

origin_img = cv2.imread('../data/logo.png')

print origin_img.shape

# zoom out the image by resize
scaleFactor = 10
rows, cols = origin_img.shape[:2]

img2 = cv2.resize(origin_img, (rows * scaleFactor, cols * scaleFactor), interpolation=cv2.INTER_LINEAR)

print img2.shape

cv2.imshow('origin img', origin_img)
cv2.imshow('scale img', img2)


cv2.waitKey(0)
cv2.destroyAllWindows()
