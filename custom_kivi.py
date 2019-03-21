from kivy.uix.widget import Widget
from kivy.uix.scatter import Scatter
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.properties import BoundedNumericProperty

class Gauge(Widget):
    value = BoundedNumericProperty(0, min=-20, max=120, errorvalue=0)
    def __init__(self, **kwargs):
        super(Gauge, self).__init__(**kwargs)
        self._gauge = Image(
            size = (320, 320),
            pos_hint={'x': 0.1, 'y': .3},
            source = './merilec/temperatura_merilec.png',
        )
        self._needle = Scatter(
            size = (320, 320),
            do_rotation = False,
            do_scale = False,
            do_translation = False
        )
        self._needle.add_widget(Image(
            source = "./merilec/needle.png",
            size = (320, 320)
        ))
        self.add_widget(self._gauge)
        self.add_widget(self._needle)
        self.bind(pos=self._update)
        self.bind(size=self._update)
        self.bind(value=self._turn)

    def _update(self, *args):
        self._gauge.pos = self.pos
        self._needle.pos = (self.x, self.y)
        self._needle.center = self._gauge.center

    def _turn(self, *args):
        self._needle.center_x = self._gauge.center_x
        self._needle.center_y = self._gauge.center_y
        self._needle.rotation = (50 * 1.8) - (self.value * 1.8)
