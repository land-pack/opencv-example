import cv2
import numpy

img = cv2.imread('../data/logo.png')
img2 = cv2.imread('../data/apple.png')


print 'origin image shape -->',img.shape
print img[10, 10]

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

print 'gray image shape -->',gray.shape
print gray[10,10]

ret, mask = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY)


print 'ret -->', ret
print 'mask -->', mask


print 'mask shape -->', mask.shape

# 
mask_inv = cv2.bitwise_not(mask)

print 'inverse mask -->', mask_inv

# 

#img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)
