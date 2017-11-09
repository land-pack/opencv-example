import numpy as np
import cv2


cap = cv2.VideoCapture(0)

while True:
	
	ret, frame = cap.read()
	
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	
	cv2.imshow('frame', gray)
	
	key = cv2.waitKey(1)
	
	if key & 0XFF == ord('q'):
		cv2.imwrite('lasteimg.png', gray)
		break


cap.release()
cv2.destroyAllWindows()
