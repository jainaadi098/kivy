from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import StringProperty

class MyShape(Widget):
    pass

class ShapeApp(App):
    def build(self):
        return MyShape()

if __name__ == '__main__':
    ShapeApp().run()