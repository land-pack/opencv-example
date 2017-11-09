import numpy as np
import cv2


cap = cv2.VideoCapture(0)

# Define the codes and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))



while True:
	
	ret, frame = cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	if ret == True:
		frame = cv2.flip(frame, 0)
	
		# Write the flipped frame
		out.write(frame)

		cv2.imshow('frame', gray)
		k = cv2.waitKey(1)
		if k & 0XFF == ord('q'):
			break
	
	else:
		break

cap.release()
out.release()
cv2.destroyAllWindows()
