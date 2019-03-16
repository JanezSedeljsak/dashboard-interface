import kivy
from kivy.app import App
from kivy.uix.slider import Slider
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle
from kivy.uix.switch import Switch
from kivy.uix.button import Button
from kivy.config import Config
from kivy.uix.stacklayout import StackLayout
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from os.path import join, dirname, abspath

# konfiguracija velikosti okna
Window.size = (1280, 640)
Window.clearcolor = (0.2, 0.2, 0.2, 0.5)

class Layout():
    @staticmethod
    def generateWidgets():
        path = dirname(abspath(__file__))
        layout = StackLayout()
        stack = []
        widgets = {
            "firstRow":[
                {"text": "[color=2a9c9d][b]Vlaga ( %d )[/b][/color]" % 15},
                {"text": "[color=B9DA6E][b]Temperatura ( %d°C )[/b][/color]" % 22},
                {"text": "[color=f98861][b]Svetlost ( %dlm )[/b][/color]" % 250}
            ],
            "secondRow": [
                {"path": str(join(path, "./vlaga_merilec.png")), 
                "pointer": {
                    "path": str(join(path, "./needle.png")),
                    "angle": 5
                }},
                {"path": str(join(path, "./temperatura_merilec.png")), 
                "pointer": {
                    "path": str(join(path, "./needle.png")),
                    "angle": 5
                }},
                {"path": str(join(path, "./svetlost_merilec.png")), 
                "pointer": {
                    "path": str(join(path, "./needle.png")),
                    "angle": 5
                }}
            ],
            
        }

        ## added top buttons

        for title in widgets["firstRow"]:
            current_widget = Label(
                text = title["text"],
                markup = True,
                font_size='37sp',
                size_hint=(1/3, 0.15)
            )
            stack.append(current_widget)


        ## added gauges

        for gauge in widgets["secondRow"]:
            current_widget = FloatLayout(
                size_hint=(1/3, 0.5)
            )
            current_widget.add_widget(Image(
                source=gauge["path"],
                size_hint=(.8, .8),
                pos_hint={'x':.1, 'y':.1}
            ))

            needle = Image(
                source=gauge["pointer"]["path"],
                size_hint=(.8, .8),
                pos_hint={'x':.1, 'y':.1}
            )
            #needle.angle = 150
            current_widget.add_widget(needle)
            
            stack.append(current_widget)

        ### bottom left content 

        def changeContent(x):
            if("ON" in x.text.upper()):
                x.text=("[color=888][b]OFF[/b][/color]")
                x.background_color=(.7, .7, .7, 1.0)

            else:
                x.text=("[color=888][b]ON[/b][/color]")
                x.background_color=(.2, .8, .3, 1.0)

        bottomLayout = FloatLayout(
            size_hint=(1, 0.35) 
        )        

        for button in range(2):
            btn = Button(
                text = "[color=888][b]OFF[/b][/color]",
                size_hint = (1/3, .4),
                pos_hint = {'x':.03, 'y': .6 if button < 1 else .1},
                border = (28,28,28,28),
                background_color = (.7, .7, .7, 1.0),
                markup = True,
                font_size = '37sp'
            )
            btn.bind(on_press = changeContent)
            bottomLayout.add_widget(btn)

        for slider in range(2):
            slider = Slider(
                min=0, max=100, value=25,
                size_hint = (3/5, .4),
                pos_hint= {'x':2/5, 'y': .6 if slider < 1 else .1},
            )   
            bottomLayout.add_widget(slider)  


        stack.append(bottomLayout)


        [layout.add_widget(widget) for widget in stack]
    
        return layout

class intefaceApp(App):
    def build(self):
        return Layout.generateWidgets()
        

if __name__ == '__main__':
    intefaceApp().run()
