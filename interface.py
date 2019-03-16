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
        if("ON" in self.btn1.text.upper()):
            self.btn1.text=("[color=888][b]OFF[/b][/color]")
            self.btn1.background_color=(.7, .7, .7, 1.0)
            self.slider1.value = 0.00

        else:
            self.slider1.value = 100.00
            self.btn1.text=("[color=888][b]ON[/b][/color]")
            self.btn1.background_color=(.2, .8, .3, 1.0)

    def btn2_click(self):
        if("ON" in self.btn2.text.upper()):
            self.btn2.text=("[color=888][b]OFF[/b][/color]")
            self.btn2.background_color=(.7, .7, .7, 1.0)
            self.slider2.value = 0.00

        else:
            self.slider2.value = 100.00
            self.btn2.text=("[color=888][b]ON[/b][/color]")
            self.btn2.background_color=(.2, .8, .3, 1.0)

    def slider1_drag(self):
        if self.slider1.value > 1.00:
            self.btn1.text=("[color=888][b]ON[/b][/color]")
            self.btn1.background_color=(.2, .8, .3, 1.0)
        else:
            self.btn1.text=("[color=888][b]OFF[/b][/color]")
            self.btn1.background_color=(.7, .7, .7, 1.0)


    def slider2_drag(self):
        if self.slider2.value > 1.00:
            self.btn2.text=("[color=888][b]ON[/b][/color]")
            self.btn2.background_color=(.2, .8, .3, 1.0)
        else:
            self.btn2.text=("[color=888][b]OFF[/b][/color]")
            self.btn2.background_color=(.7, .7, .7, 1.0)


class InterfaceApp(App):
    def build(self):
        return Controller()

if __name__ == '__main__':
    InterfaceApp().run()