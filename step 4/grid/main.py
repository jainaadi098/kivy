from kivy.app import App
from kivy.uix.gridlayout import GridLayout

class MyGrid(GridLayout):
    pass

class GridApp(App):
    def build(self):
        return MyGrid()

if __name__ == '__main__':
    GridApp().run()
    