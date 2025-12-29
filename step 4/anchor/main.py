from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout

class MyAnchor(AnchorLayout):
    pass

class AnchorApp(App):
    def build(self):
        return MyAnchor()

if __name__ == '__main__':
    AnchorApp().run()