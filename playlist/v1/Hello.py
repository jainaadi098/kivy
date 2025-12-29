
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class Hello(BoxLayout):
    pass

class HelloWorld(App):
    def build(self):
        # return Label(text='Hello, World!')
        return Hello()

HelloWorld().run()