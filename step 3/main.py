from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class MyLayout(BoxLayout):
    # This function changes the text
    def change_text(self):
        # 1. Go to the list of IDs (self.ids)
        # 2. Find the widget named 'my_label'
        # 3. Change its text property
        self.ids.my_label.text = "You clicked it!"
    
    
    

class TestApp(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    TestApp().run()