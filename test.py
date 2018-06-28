import kivy
from random import random
from track import *

kivy.require('1.1.0') # replace with your current kivy version !

from kivy.core.window import Window
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

class MyApp(App):
    def build(self):
        self.main_box = BoxLayout(orientation='vertical')        
        self.button = Button(text='label', font_size=20, font_name='Roboto')
        self.button2 = Button(text='label', font_size=15, font_name='Roboto')
        self.track = Track('CAC', (1/8))
        self.track.addRunner(Runner(120, 'Stan', '000'))
        self.track.addCurrentRunner(self.track.runners[0])
        self.track.addRunner(Runner(150, 'Jane', '001'))
        self.track.addCurrentRunner(self.track.runners[1])
        self.track.addRunner(Runner(135, 'John', '002'))
        self.track.addCurrentRunner(self.track.runners[2])
        self.track.addRunner(Runner(125, 'Dan', '003'))
        self.track.addCurrentRunner(self.track.runners[3])
        self.track.addRunner(Runner(140, 'Jill', '004'))
        self.track.addCurrentRunner(self.track.runners[4])
        self.track.addRunner(Runner(145, 'Steve', '005'))
        self.track.addCurrentRunner(self.track.runners[5])
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)
        self.main_box.add_widget(self.button)
        self.main_box.add_widget(self.button2)
        Clock.schedule_interval(self.leaderboard, 0.01)
        Clock.schedule_interval(self.currentRunnerStats, 0.01)
        return self.main_box
    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        if keycode[1] == '`':
            for i in range(len(self.track.currentRunners)):
                self.track.currentRunners[i].addLap(random() * 700)
    def leaderboard(self, dt):
        self.button.text = self.track.leaderboard.stringIt()
    def currentRunnerStats(self, dt):
        self.button2.text = 'Current Runners: \n name          fastest lap          last lap          total laps          mi ran          kCal burned          average speed \n'
        for i in range(len(self.track.currentRunners)):
            self.button2.text += '{:<20}'.format(str(self.track.currentRunners[i].name)[:20])
            self.button2.text += self.track.currentRunners[i].currentSession.stringIt()
    
if __name__ == '__main__':
    MyApp().run()
        
