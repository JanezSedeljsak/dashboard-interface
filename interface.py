import kivy
from kivy.app import App
from kivy.uix.stacklayout import StackLayout
from kivy.core.window import Window

Window.size = (1280, 640)
Window.clearcolor = (0.2, 0.2, 0.2, 0.5)

class Controller(StackLayout):
    def __init__(self):
        super(Controller, self).__init__()

    def btn_click(self, btn, slider): slider.value = 100.00 if "ON" not in btn.text.upper() else 0.00

    def slider_drag(self, btn, slider):
        if slider.value > 1.00:
            btn.text=("[color=888][b]ON[/b][/color]")
            btn.background_color=(.2, .8, .3, 1.0)
        else:
            btn.text=("[color=888][b]OFF[/b][/color]")
            btn.background_color=(.7, .7, .7, 1.0)

class InterfaceApp(App):
    build = lambda self: Controller()

InterfaceApp().run() if __name__ == '__main__' else None