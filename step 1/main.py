# 1. Import the necessary tools
from kivy.app import App
from kivy.uix.label import Label

# 2. Create your App class (The Director)
class MyApp(App):
    def build(self):
        # This function returns the "Root Widget" - the main thing on screen
        return Label(text='Hello, Kivy!')

# 3. Run the app
if __name__ == '__main__':
    MyApp().run()