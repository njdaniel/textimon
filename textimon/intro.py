import kivy

from kivy.app import App
from kivy.uix.label import Label

class Intro(App):

    def run(self):
        return Label(text='Test This')

if __name__=='__main__':
    Intro().run()
