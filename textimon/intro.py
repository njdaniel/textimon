#!/Users/nicholas/PycharmProjects/textimon/textimonenv/bin/python
import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.button import Label

class IntroApp(App):

    def build(self):
        return Label()

if __name__=='__main__':
    intro = IntroApp()
    intro.run()
