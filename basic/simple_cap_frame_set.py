import numpy as np
import cv2



cap = cv2.VideoCapture(0)

print 'current capture width: ', cap.get(3)
print 'current capture height: ', cap.get(4)


cap.set(3, 128)
cap.set(4, 72)

while True:
	
	ret, frame = cap.read()

	# Our operation on the frame code here

	
	gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
	cv2.imshow('frame', gray)
	if cv2.waitKey(1) & 0XFF == ord('q'):
		break

# When everthing done, release the capture .

cap.release()
cv2.destroyAllWindows()
