import numpy as np
import cv2

cap = cv2.VideoCapture(0)
smile_cascade = cv2.CascadeClassifier('hand_cascade_stage8.xml')
while(True):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if np.any(smile_cascade.detectMultiScale(gray, 1.3, 5)):
    	smile = smile_cascade.detectMultiScale(gray, 1.3, 5)
    	print "hand found"
    	break
    	for (x,y,w,h) in smile:
    		cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 2)
    else:
    	print "Lost it"

    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()