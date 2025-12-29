from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class BoxApp(App):
    def build(self):
        # 1. Create the Layout
        # orientation='vertical' stacks them. 
        # padding=20 adds space around the edges.
        # spacing=10 adds space between the buttons.
        layout = BoxLayout(orientation='vertical', padding=0, spacing=0)

        # 2. Create Buttons
        btn1 = Button(text='First')
        btn2 = Button(text='Second')
        btn3 = Button(text='Third')

        # 3. Add Buttons to Layout
        layout.add_widget(btn1)
        layout.add_widget(btn2)
        layout.add_widget(btn3)

        # 4. Return the Layout to show it
        return layout

if __name__ == '__main__':
    BoxApp().run()