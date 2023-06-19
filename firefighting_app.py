from kivy.app import App
from kivy.core.window import Window
#from kivymd.app import MDApp
#from kivymd.uix.card import MDCard
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.garden.joystick import Joystick
from kivy.clock import Clock
from kivy.graphics.texture import Texture
from kivy.uix.floatlayout import FloatLayout


from array import array
import time

import cv2
from PyQt5 import QtCore, QtGui, QtWidgets

Window.clearcolor = (0,0,0)
Window.size = (400,600)






class MainWindow(Screen):
    pass
class SecondWindow(Screen):
    def update_camera_feed(self, dt):
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        if ret:
            buf1 = cv2.flip(frame, 0)
            buf = buf1.tostring()
            texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
            texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
            self.ids.camera_feed.texture = texture
        cap.release()
        Clock.schedule_interval(self.root.get_screen('second').update_camera_feed, 1.0/30.0)
    pass
class windowManger(ScreenManager):
    pass


KV = Builder.load_file('project.kv')

# the Base Class of our Kivy App
class myapp(App):
    def build(self):
        self.title = 'firefighting ropot app'

        
        return KV






    



if __name__ == '__main__':
   myapp().run()