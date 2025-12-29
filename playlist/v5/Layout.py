from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class boxlayoutclass(BoxLayout):
    def __init__(self,**kwargs):
        super(boxlayoutclass, self).__init__(**kwargs)
        self.orientation='vertical'
        button = Button(text='Hello')
        self.add_widget(button)
        button1 = Button(text='A',size_hint=(None,None),size=(1920,50))
        self.add_widget(button1)
        button2 = Button(text='B')
        self.add_widget(button2)


class layoutApp(App):
    def build(self):
        return boxlayoutclass()

layoutApp().run()