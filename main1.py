import kivy
from kivy.app import App
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
import os
kivy.require("1.11.1")
class MyPage(GridLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.cols=2
        if(os.path.isfile("PreviousDetails.txt")):
            with open("PreviousDetails.txt","r") as f:
                d=f.read().split(',')
                p1=d[0]
                p2=d[1]
                p3=d[2]
        else:
            p1=""
            p2=""
            p3=""
        self.add_widget(Label(text="Name:"))
        self.name=TextInput(text=p1,multiline=False)
        self.add_widget(self.name)
        self.add_widget(Label(text="Branch:"))
        self.branch=TextInput(text=p2,multiline=False)
        self.add_widget(self.branch)
        self.add_widget(Label(text="Year:"))
        self.year=TextInput(text=p3,multiline=False)
        self.add_widget(self.year)
        self.join=Button(text="Enter here",size_hint=(1, .3),color=(1,1,0,1))
        self.join.bind(on_press=self.myfunction)
        self.add_widget(self.join)
    def myfunction(self,instance):
        a=self.name.text
        b=self.branch.text
        c=self.year.text
        print(a," ",b," ",c)
        with open("PreviousDetails.txt","w") as f:
            f.write(f"{a},{b},{c}")
        chat.screen_manager.current="Another"

class Another(GridLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            self.color=Color(1,.5,.6,mode="rgb")
            self.rect = Rectangle(pos=self.pos, size=self.size)
        #self.bind(pos=self.update_rect)
        self.bind(size=self.update_rect)
        self.cols=1
        self.message=Label(halign="center",valign="center",font_size=30,color=(0,1,.5,1))
        #self.message.bind(width=self.update_text_width)
        self.message.text="Hello World"
        self.add_widget(self.message)
    def update_rect(self,*_):
        self.rect.pos=self.pos
        self.rect.size=self.size
class Ok(BoxLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        layout=BoxLayout(orientation='vertical')
        btn1=Button(text='hello',size=(20,30))
        btn2=Button(text="Hey there")
        btn2.bind(on_press=self.camerafuc)
        # anim=Animation(x=50)
        # anim.start(btn2)
        layout.add_widget(btn1)
        layout.add_widget(btn2)
        #layout.add_widget(Slider(orientation='vertical',min=-100, max=100, value=25,value_track=True,value_track_color=[1, 0, 0, 1]))
        self.add_widget(layout)
    def camerafuc(self,instance):
        cam=Camera(play=False)
class MyApp(App):
    def build(self):
        self.icon = '1.jpeg'
        print(self.get_application_icon())
        self.screen_manager=ScreenManager()
        self.connect=MyPage()
        screen=Screen(name="Connect")
        screen.add_widget(self.connect)
        self.screen_manager.add_widget(screen)
        self.another=Another()
        screen=Screen(name="Another")
        screen.add_widget(self.another)
        self.screen_manager.add_widget(screen)
        return self.screen_manager

if __name__=="__main__":
    chat=MyApp()
    chat.run()
