from kivy import *

from kivy.app import App
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
            "thirdRow": {
                "leftBottomButton": {
                    "text": "[color=888][b]OFF[/b][/color]",
                    "width": 1/3,
                    "innerSize": {"x": .9, "y": .4},
                    "margin": {"x": .05, "y": .3},
                    "afterClick": [
                        "[color=888][b]OFF[/b][/color]",
                        "[color=888][b]ON[/b][/color]"
                        ],
                    "border":(28,28,28,28)
                }
            },
            
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

        leftButton = widgets["thirdRow"]["leftBottomButton"]
        leftButtonParent = FloatLayout(
            size_hint=(leftButton["width"], 0.35)
        )
        button = Button(
            text = leftButton["text"],
            size_hint = (leftButton["innerSize"]["x"], leftButton["innerSize"]["y"]),
            pos_hint= {'x':leftButton["margin"]["x"], 'y': leftButton["margin"]["y"]},
            border = leftButton["border"],
            background_color = (.7, .7, .7, 1.0),
            markup = True,
            font_size = '37sp'
        )
        button.bind(on_press = changeContent)
        leftButtonParent.add_widget(button)
        stack.append(leftButtonParent)


        leftButton = widgets["thirdRow"]["leftBottomButton"]
        leftButtonParent = FloatLayout(
            size_hint=(leftButton["width"], 0.35)
        )
        button = Button(
            text = leftButton["text"],
            size_hint = (leftButton["innerSize"]["x"], leftButton["innerSize"]["y"]),
            pos_hint= {'x':leftButton["margin"]["x"], 'y': leftButton["margin"]["y"]},
            border = leftButton["border"],
            background_color = (.7, .7, .7, 1.0),
            markup = True,
            font_size = '37sp'
        )
        button.bind(on_press = changeContent)
        leftButtonParent.add_widget(button)
        stack.append(leftButtonParent)


##        #### bottom right content
##        stack.append(Switch(
##            active=False,
##            size_hint=(1/3, 0.15)
##        ))
##        stack.append(Switch(
##            active=True,
##            size_hint=(1/3, 0.15)
##        ))
            

        [layout.add_widget(widget) for widget in stack]
    
        return layout

class intefaceApp(App):
    def build(self):
        return Layout.generateWidgets()
        

if __name__ == '__main__':
    intefaceApp().run()
