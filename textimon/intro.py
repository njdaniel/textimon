#!/Users/nicholas/PycharmProjects/textimon/textimonenv/bin/python
import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.button import Label

class Intro(App):

    def build(self):
        return Label(text='Test This')

if __name__=='__main__':
    intro = Intro()
    intro.run()
