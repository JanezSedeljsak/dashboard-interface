import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from threading import Timer
from kivy.animation import Animation
from kivy.config import Config
from custom_kivi import Gauge

[Config.set('graphics', x, y) for x, y in {'resizable': '0', 'width': '1280', 'height': '640'}.items()]

class Controller(FloatLayout):
    def __init__(self):
        super(Controller, self).__init__()
        self.updateGauges()

    def updateGauges(self):
        try:
            w = self
            values = [int(x.split(':')[1]) for x in open("./values.txt", 'r').readline().split(" ")]
            w.label1.text = '[color=2a9c9d][b]Vlaga (%d)[/b][/color]' % values[0]
            w.label2.text = '[color=B9DA6E][b]Temperatura (%d)[/b][/color]' % values[1]
            w.label3.text = '[color=f98861][b]Svetlost (%d)[/b][/color]' % values[2]
            [Animation(value = values[i]).start(x) for i, x in enumerate([w.gauge1, w.gauge2, w.gauge3])]

        except:
            print("error occured")

        Timer(1, self.updateGauges).start()

    def btn_click(self, btn, slider): slider.value = float(100) if "ON" not in btn.text.upper() else float(0)

    def slider_drag(self, btn, slider):
        [setattr(btn, x, y) for x, y in {
            "text": "[color=888][b]ON[/b][/color]" if slider.value > float(1) else "[color=888][b]OFF[/b][/color]", 
            "background_color": (.4, .8, .9, 1.0) if slider.value > float(1) else (.7, .7, .7, 1.0)
        }.items()]

class InterfaceApp(App): 
    build = lambda self: Controller()

InterfaceApp().run() if __name__ == '__main__' else None