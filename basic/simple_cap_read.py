import numpy as np
import cv2

cap = cv2.VideoCapture(0) # Device index is just the number to specify which camera.


while True:
	# Capture frame-by-frame
	ret, frame = cap.read()

	# Our operations on the frame come here
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	print 'ret >>>', ret
	# Display the resulting frame
	cv2.imshow('frame', gray)
	if cv2.waitKey(1) & 0XFF == ord('q'):
		break



# When everthing done, release the capture
cap.release()
cv2.destroyAllWindows()
