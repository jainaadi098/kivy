import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.core.window import Window


Window.size = (350, 600)
Builder.load_file('Calculator1.kv')

class Calculator(Widget):
    pass

class Calculator_1App(App):
    def build(self):
        
        return Calculator()

Calculator_1App().run()