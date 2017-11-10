import numpy as np
import cv2


img = np.zeros((512, 512, 3), np.uint8)

# Draw a diagonal red circle with thickness of 3 px

cv2.circle(img, (50, 50), 63, (0, 0, 255), -1)
cv2.circle(img, (250, 250), 63, (0, 78, 55), 4)


cv2.imshow('circle', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
