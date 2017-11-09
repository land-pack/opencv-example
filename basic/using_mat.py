import numpy as np
from matplotlib import pyplot as plt
import cv2


img = cv2.imread("apple.png", 0)

plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.xticks([]), plt.xticks([]) # To hide tick values on X and Y axis
plt.show()
