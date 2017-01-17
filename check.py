import numpy as np
import cv2
import os
from kivy.uix.widget import Widget 
from kivy.event import EventDispatcher
from kivy.properties import NumericProperty, StringProperty




class FaceLock(Widget):
    cascade = StringProperty()

    index = NumericProperty(0)

    
    
    def __init__(self, **kwargs):
        self.register_event_type('on_match')
        super(FaceLock, self).__init__(**kwargs)
        self.face_recognize()

    def on_match(self):
        pass
    def face_recognize(self):
        cap = cv2.VideoCapture(self.index)
        face_cascade = cv2.CascadeClassifier(self.cascade)
        while(True):
            ret, frame = cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            if np.any(face_cascade.detectMultiScale(gray, 1.3, 5)):
                
                print ("Cascade found")
                
                self.dispatch('on_match')
                
                cv2.destroyAllWindows()
                for i in range(1,5):
                    cv2.waitKey(1)
                break
            else:
                print ("Not recognized")

            cv2.imshow('frame',frame)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                print ("Forcefully Closed")
                
                cv2.destroyAllWindows()
                for i in range(1,5):
                    cv2.waitKey(1)
                break
        cap.release()