import cv2
import numpy

img = cv2.imread('../data/logo.png')

print 'origin image shape -->',img.shape
print img[10, 10]

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

print 'gray image shape -->',gray.shape
print gray[10,10]

