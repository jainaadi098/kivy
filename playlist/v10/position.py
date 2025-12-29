from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label



class sizechange(FloatLayout):
    
    def __init__(self, **kwargs):
        self.text='Hello'
        
        super(sizechange,self).__init__(**kwargs)
        button= Button(text="Click 1",size_hint=(.2,.2),pos=(100,100))
        self.add_widget(button)
        button1= Button(text="Click 2",size_hint=(.2,.2),pos_hint={'x':.3,'y':.3})
        self.add_widget(button1)
        button2= Button(text="Click 3",size_hint=(.2,.2),pos_hint={'x':.5,'y':.5})
        self.add_widget(button2)
        
        label=Label(text=self.text,pos_hint={'x':.5,'y':.5},size_hint=(-.2,.2))
        self.add_widget(label)
        


class posiApp(App):
    def build(self):
        return sizechange()

posiApp().run()