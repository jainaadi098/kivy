from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

ChangeSize=Builder.load_file('sizechange.kv')

class sizechange(BoxLayout):
    pass

class SizeApp(App):
    def build(self):
        return sizechange()

SizeApp().run()