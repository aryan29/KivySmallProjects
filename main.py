
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.layout import Layout
from kivy.uix.screenmanager import ScreenManager,Screen,FadeTransition,SlideTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color,Rectangle,Line
from kivy.uix.slider import Slider
from kivy.animation import Animation
from kivy.uix.camera import Camera
from kivy.network.urlrequest import UrlRequest
import os
import certifi as cfi
class MyApp(App):
    def build(self):
        return ScreenManagement(transition=SlideTransition())
class ScreenManagement(ScreenManager):
    pass
class Screen1(Screen):
    pass
class Screen2(Screen):
    def on_enter(self, *args):
        user=self.manager.ids.sc1.display.text
        print(user)
        def bug_posted(x, result):
            print('An error is detected',result['comment'])
            label=self.ids['labeltext']
            label.text=result['comment']
        x=UrlRequest(f"https://codeforces.com/api/user.info?handles={user}",on_failure=bug_posted,ca_file=cfi.where(), verify=True)
        x.wait()
        try:
            rating=x.result['result'][0]['rating']
            print(rating)
            label=self.ids['labeltext']
            label.text=f"User {user} rating is {rating}"
        except:
            print("Already given error report")
class Screen3(Screen):
    def on_touch_down(self, touch):
        print(touch)
        with self.canvas:
            Color(1,1,0)
            touch.ud["line"] = Line(points=(touch.x, touch.y),width=10)
    def on_touch_move(self, touch):
        print(touch)
        touch.ud["line"].points += (touch.x, touch.y)
    def on_touch_up(self, touch):
        print("RELEASED!",touch)
        #Screen.name="hello"
class Screen4(Screen):
    pass
class Screen5(Screen):
    def function(self):
        self.manager.ids.sc3.canvas.add(Color(1., 1., 0))
        print("hello")


Builder.load_file('a.kv')
if __name__=="__main__":
    chat=MyApp()
    chat.run()
