
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.layout import Layout
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color,Rectangle
from kivy.uix.slider import Slider
from kivy.animation import Animation
from kivy.uix.camera import Camera
import requests
import os
class MyApp(App):
    def build(self):
        return ScreenManagement()
class ScreenManagement(ScreenManager):
    pass
class Screen1(Screen):
    pass
class Screen2(Screen):
    def on_enter(self, *args):
        user=self.manager.ids.sc1.display.text
        x=requests.get(f"https://codeforces.com/api/user.info?handles={user}")
        a=x.json()
        rating=a['result'][0]['rating']
        label=self.ids['labeltext']
        label.text=f"User {user} rating is {rating}"


Builder.load_file('a.kv')
if __name__=="__main__":
    chat=MyApp()
    chat.run()
