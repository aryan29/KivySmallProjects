from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.graphics import Line,Color
from kivy.uix.screenmanager import  ScreenManager,Screen,FadeTransition,SlideTransition
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
import random
# class wids(Widget):
#     pass
class ScreenManagement(ScreenManager):
        pass
class MainScreen(Screen):
    pass
class OneMore(Screen):
    def change_label(self,*args):
        label=self.ids['mylabel']
        print(len(label.text))
        label.color=(1,0,1,1)
    def on_enter(self, *args):
        label=self.ids['mylabel']
        print(len(label.text))
        if(label.text==''):
            label.text="hello new buddy"
class DrawInput(Screen):

    def on_touch_down(self, touch):
        print(touch)
        with self.canvas:
            Color(1, 0,2)
            touch.ud["line"] = Line(points=(touch.x, touch.y),width=10)

    def on_touch_move(self, touch):
        print(touch)
        touch.ud["line"].points += (touch.x, touch.y)

    def on_touch_up(self, touch):
        print("RELEASED!",touch)
Builder.load_file('MyApp.kv')
class MyApp(App):
    def build(self):
        return ScreenManagement()
if __name__=="__main__":
    MyApp().run()
