import cv2
import numpy as np
from kivy.app import App 
from kivy.lang import Builder
from kivy.uix.label import Label 
from kivy.uix.screenmanager import Screen, ScreenManager, FadeTransition
Builder.load_string('''
<StartScreen>:
	BoxLayout:
		orientation: 'vertical'
		# Camera:
		# 	id: camera
		# 	resolution: (1024, 1024)
		Button:
			id: btn
			text: "hello"
			on_press: root.Finger_gesture()


''')


class StartScreen(Screen):
	def Finger_gesture(self):
		cap = cv2.VideoCapture(0)
		smile_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
		while(True):
		    ret, frame = cap.read()
		    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		    if np.any(smile_cascade.detectMultiScale(gray, 1.3, 5)):
		    	smile = smile_cascade.detectMultiScale(gray, 1.3, 5)
		    	print "hand found"
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
		        # return 0
		        break
		self.test_func()
		cap.release()
		# cv2.destroyAllWindows()
	def test_func(self):
		print "2+2 is : 4"


sm = ScreenManager(transition=FadeTransition())
sm.add_widget(StartScreen(name="start"))

class CameraApp(App):
	def build(self):
		return sm

CameraApp().run()