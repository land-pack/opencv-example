import numpy as np
import cv2


img = cv2.imread("apple.png")

cv2.imshow('image', img)

#k = cv2.waitKey(0)

# Warning: If you are using a 64-bit machine, you will
# have to modify k = cv2.waitKey(0) line as follows:
k = cv2.waitKey(0) & 0xFF

if k == 27: # Wait for ESC key to exit
	cv2.destroyAllWindows()
elif k == ord('s'): # Wait for 's' key to save and exit
	cv2.imwrite('messigray.png', img)
	cv2.destroyAllWindows()


