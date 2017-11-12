import numpy as np
import cv2


# Create a  black image

img = np.zeros((512, 512, 3), np.uint8)

cv2.rectangle(img, (1,1), (500, 500), (0, 255, 0), 3)



cv2.imshow('frame', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
# 
