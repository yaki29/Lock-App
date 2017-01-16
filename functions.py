from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior


class MyButton(ButtonBehavior, Image):
    def __init__(self, **kwargs):
        super(MyButton, self).__init__(**kwargs)
        self.source = '1.jpg'

    def on_press(self):
        self.source = '4.jpg'

    def on_release(self):
        self.source = 'yash.jpg'


class SampleApp(App):
    def build(self):
        return MyButton()
SampleApp().run()
