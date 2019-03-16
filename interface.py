import kivy
from kivy.app import App
from kivy.uix.popup import Popup
from kivy.uix.stacklayout import StackLayout
from kivy.core.window import Window
kivy.require('1.9.1')

# konfiguracija velikosti okna
Window.size = (1280, 640)
Window.clearcolor = (0.2, 0.2, 0.2, 0.5)


class Controller(StackLayout):
    def __init__(self):
        super(Controller, self).__init__()

    def btn1_click(self):
        if("ON" in self.text.upper()):
            self.text=("[color=888][b]OFF[/b][/color]")
            self.background_color=(.7, .7, .7, 1.0)
            self._0_slider.value = 32.4324234

        else:
            self.text=("[color=888][b]ON[/b][/color]")
            self.background_color=(.2, .8, .3, 1.0)

    def btn2_click(self):
        if("ON" in self.text.upper()):
            self.text=("[color=888][b]OFF[/b][/color]")
            self.background_color=(.7, .7, .7, 1.0)
            self._0_slider.value = 32.4324234

        else:
            self.text=("[color=888][b]ON[/b][/color]")
            self.background_color=(.2, .8, .3, 1.0)

    def slider1_drag(self):
        self.lbl.text = "You have been pressed"

    def slider2_drag(self):
        self.lbl.text = "You have been pressed"


class InterfaceApp(App):
    def build(self):
        return Controller()

if __name__ == '__main__':
    InterfaceApp().run()