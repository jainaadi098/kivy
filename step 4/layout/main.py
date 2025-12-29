from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty # <--- Import the magic

class MyLayout(BoxLayout):
    # Define the magic variable
    # We give it a default value of "0"
    my_text = StringProperty("0")

    def increment(self):
        # We turn the text into an int, add 1, then turn it back to string
        current_val = int(self.my_text)
        current_val += 1
        self.my_text = str(current_val) # <--- The screen updates AUTOMATICALLY here!

class CounterApp(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    CounterApp().run()