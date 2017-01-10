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
			text: "hello"
			on_press: root.Finger_gesture()





''')


class StartScreen(Screen):
	def Finger_gesture(self):
		cap = cv2.VideoCapture(0)
		
		while(True):
		    ret, frame = cap.read()
		    cv2.imshow('frame',frame)
		    if cv2.waitKey(1) & 0xFF == ord('q'):
		        break
		cap.release()
		# cv2.destroyAllWindows()
		


sm = ScreenManager(transition=FadeTransition())
sm.add_widget(StartScreen(name="start"))

class CameraApp(App):
	def build(self):
		return sm

CameraApp().run()