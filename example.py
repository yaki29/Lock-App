from check import FaceLock
from kivy.app import App 
from kivy.lang import Builder
from kivy.uix.label import Label 
from kivy.uix.screenmanager import Screen, ScreenManager, FadeTransition
Builder.load_string('''
<StartScreen>:
	BoxLayout:
		orientation: 'vertical'
		Label:
			id: lbl
			text: "You have a nice face !!!"
			font_size: 40
<LockScreen>:
	
	index: 0
	cascade: 'haarcascade_frontalface_default.xml'
	on_match: root.change_scr()
	BoxLayout: 
		Label: 
			text: "Same Screen"
			font_size: 40
		Button:
			text: "change"
			on_press: root.manager.current = "application_screen"

''')


class StartScreen(Screen):
	pass
class LockScreen(FaceLock, Screen):
	def change_scr(self):
		print "Screen Changing" 
		sm.current = "application_screen"

sm = ScreenManager(transition=FadeTransition())
sm.add_widget(StartScreen(name="application_screen"))
sm.add_widget(LockScreen(name="lock_screen"))

class CameraApp(App):
	sm.current = "lock_screen"
	def build(self):
		return sm

CameraApp().run()