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
            values = []
            for x in open("./values.txt", 'r').readline().split(" "):
                values.append(int(x.split(':')[1]))
                
            self.label1.text = '[color=2a9c9d][b]Vlaga (%d)[/b][/color]' % values[0]
            self.label2.text = '[color=B9DA6E][b]Temperatura (%d)[/b][/color]' % values[1]
            self.label3.text = '[color=f98861][b]Svetlost (%d)[/b][/color]' % values[2]

            for i in range(len(values)):
                if values[i]<-20:
                    values[i]=-20
                elif values[i]>120:
                    values[i]=120
                    
            Animation(value = values[0]).start(self.gauge1)
            Animation(value = values[1]).start(self.gauge2)
            Animation(value = values[2]).start(self.gauge3)

        except:
            print("error occured")

        Timer(1, self.updateGauges).start()

    def btn_click(self, btn, slider): 
        if "ON" not in btn.text.upper():
            slider.value = float(100)  
        else:
            slider.value = float(0)

    def slider_drag(self, btn, slider):
        if slider.value > float(1):
            btn.text = "[color=888][b]ON[/b][/color]"
            btn.background_color = (.4, .8, .9, 1.0)
        else:
            btn.text = "[color=888][b]OFF[/b][/color]"
            btn.background_color = (.7, .7, .7, 1.0)

class InterfaceApp(App): 
    build = lambda self: Controller()

InterfaceApp().run() if __name__ == '__main__' else None
