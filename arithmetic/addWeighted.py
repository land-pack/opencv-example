import numpy as np
import cv2


img1 = cv2.imread("../data/apple.png")
img2 = cv2.imread("../data/robo.png")

img1 = img1[20:200]
print img1

img2 = img2[20:200]

dst = cv2.addWeighted(img1, 0.7, img2, 0.3, 0)

cv2.imshow('dst', dst)
cv2.waitKey(0)

cv2.destroyAllWindows()
