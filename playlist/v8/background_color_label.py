import kivy
from kivy.app import App
from kivy.lang import Builder


Hello=Builder.load_file('xyz.kv')

class LabelApp(App):
    def build(self):
        return Hello

LabelApp().run()