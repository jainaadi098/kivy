from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout

class GridApp(App):
    def build(self):
        # 1. Create the Layout
        # We set cols=2. Kivy will automatically create new rows as needed.
        layout = GridLayout(cols=1, padding=10, spacing=0)

        # 2. Add 4 Buttons directly
        layout.add_widget(Label(text='Hi '))
        layout.add_widget(Button(text='Button 2'))
        layout.add_widget(Label(text='box 3'))
        layout.add_widget(Button(text='Button 4'))

        # 3. Return the Layout
        return layout

if __name__ == '__main__':
    GridApp().run()