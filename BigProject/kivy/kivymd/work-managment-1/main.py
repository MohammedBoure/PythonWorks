from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.menu import MDDropdownMenu
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
import DataBase
import MDFiles.ScreenManagerMD
import MDFiles.MainScreenMD
import MDFiles.InputScreenMD
import MDFiles.Screen2MD
import MDFiles.Screen3MD




KV = ScreenManagerMD.code + MainScreenMD.code + InputScreenMD.code + Screen2MD.code + Screen3MD.code



class MainScreen(Screen):
    pass

class InputScreen(Screen):
    def execute(self):
        DataBase.insert_data_employees(self.ids.input1.text, self.ids.input2.text,self.ids.input3.text,self.ids.input4.text, self.ids.input5.text,self.ids.input6.text,self.ids.input7.text)

class Screen2(Screen):
    def change_color(self):
        self.ids.label.color = (1, 0, 0, 1)  # Change text color to red

class Screen3(Screen):
    def display_message(self):
        self.ids.label.text = "Hello from Page 3!"

class MainApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def change_screen(self, screen_name):
        self.root.current = screen_name

if __name__ == '__main__':
    MainApp().run()
