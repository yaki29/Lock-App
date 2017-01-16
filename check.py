import numpy as np
import cv2
import os
from kivy.uix.widget import Widget 
from kivy.event import EventDispatcher
from kivy.uix.behaviors import ButtonBehavior
from kivy.properties import OptionProperty, ObjectProperty, NumericProperty, \
    ReferenceListProperty, BooleanProperty, ListProperty, AliasProperty, \
    StringProperty



# class P(BoxLayout):

#     def __init__(sef, **kwargs):
#         super(P, self).__init__(**kwargs)
#         self.register_event_type('on_match')


#     def on_match(self):
#         screen_manager.current = 'next_creen'

#     def on_press(self):
#         print "sidhciusdcius"


class FaceLock(Widget):
    cascade = StringProperty()

    index = NumericProperty(0)
    print "Not called"
    __events__ = ('on_brick_breacked', )
    def on_brick_breacked(instance, *args):
        pass
    def __init__(self, **kwargs):
        self.register_event_type('on_match')
        super(FaceLock, self).__init__(**kwargs)
        self.face_recognize()

    def on_match(self):
        pass
    def face_recognize(self):
        cap = cv2.VideoCapture(self.index)
        smile_cascade = cv2.CascadeClassifier(self.cascade)
        while(True):
            ret, frame = cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            if np.any(smile_cascade.detectMultiScale(gray, 1.3, 5)):
                smile = smile_cascade.detectMultiScale(gray, 1.3, 5)
                print "hand found"
                self.dispatch('on_match')
                print "after dispatch"
                cv2.destroyAllWindows()
                for i in range(1,5):
                    cv2.waitKey(1)
                break
                for (x,y,w,h) in smile:
                    cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 2)
            else:
                print "Lost it"

            cv2.imshow('frame',frame)
            print "yash"
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                print "hey q pressed"
                
                cv2.destroyAllWindows()
                for i in range(1,5):
                    cv2.waitKey(1)
                break
        cap.release()
