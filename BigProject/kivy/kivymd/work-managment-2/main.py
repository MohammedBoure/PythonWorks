from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

import sys
import os

import DataBase
sys.path.append(os.path.join(os.path.dirname(__file__), 'FrontEnd'))
import MainFrontEnd

Window.size = (360, 640)

KV = """
BoxLayout:
    orientation: 'vertical'

    ScreenManager:
        id: screen_manager

        MDScreen:
            name: 'create_profile'
            BoxLayout:
                orientation: 'vertical'
                padding: 20
                spacing: 20
                MDTopAppBar:
                    title: "Create Profile"
                    elevation: 10
                ScrollView:
                    id: scroll_view
                    do_scroll_x: False
                    do_scroll_y: True
                    MDBoxLayout:
                        id: text_box
                        orientation: 'vertical'
                        size_hint_y: None
                        height: self.minimum_height
                        padding: [10, 10]
                        spacing: 20
                        MDTextField:
                            id: input1
                            hint_text: "Full name of the employee"
                        MDTextField:
                            id: input2
                            hint_text: "Number phone"
                        MDTextField:
                            id: input3
                            hint_text: "Date"
                        MDTextField:
                            id: input4
                            hint_text: "Type of car"
                        MDTextField:
                            id: input5
                            hint_text: "Description"
                        MDTextField:
                            id: input6
                            hint_text: "Been worked on"
                        MDTextField:
                            id: input7
                            hint_text: "Price"
                        MDRaisedButton:
                            text: "Execute"
                            size_hint_y: None
                            height: "56dp"
                            pos_hint: {'center_x': 0.5}
                            on_release: root.execute()
            MDCard:
                size_hint_y: None
                height: dp(30)
                elevation: 10
                md_bg_color: app.theme_cls.primary_color
                padding: dp(10)
                radius: [25, 25, 0, 0]
                MDLabel:
                    text: "Create Profile"
                    halign: "center"
                    theme_text_color: "Custom"
                    text_color: 1, 1, 1, 1

        MDScreen:
            name: 'search'
            MDBoxLayout:
                orientation: 'vertical'
                MDCard:
                    size_hint: None, None
                    size: "280dp", "280dp"
                    pos_hint: {"center_x": .5}
                    padding: "8dp"
                    MDLabel:
                        id: label
                        text: "Another Card"
                        halign: "center"
                MDTextField:
                    id: user_input
                    hint_text: "Enter text here"
                    size_hint_x: None
                    width: "280dp"
                    pos_hint: {"center_x": .5}
                MDRaisedButton:
                    text: "Submit"
                    size_hint_x: None
                    width: "280dp"
                    pos_hint: {"center_x": .5}
                    on_release: app.update_label()

    MDCard:
        size_hint_y: None
        height: dp(50)
        elevation: 10
        padding: dp(0)
        radius: [0, 0, 25, 25]
        md_bg_color: app.theme_cls.bg_dark
        ScrollView:
            do_scroll_x: True
            do_scroll_y: False
            MDGridLayout:
                cols: 5
                adaptive_width: True
                padding: dp(2)
                spacing: dp(25)
                MDIconButton:
                    icon: 'file-plus'
                    user_font_size: '48sp'
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    theme_text_color: "Custom"
                    text_color: 1, 1, 1, 1
                    on_release: app.change_screen('create_profile')
                MDIconButton:
                    icon: 'magnify'
                    user_font_size: '48sp'
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    theme_text_color: "Custom"
                    text_color: 1, 1, 1, 1
                    on_release: app.change_screen('search')
                MDIconButton:
                    icon: 'clock-outline'
                    user_font_size: '48sp'
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    theme_text_color: "Custom"
                    text_color: 1, 1, 1, 1
                    on_release: app.change_screen('to_day_work')
                MDIconButton:
                    icon: 'pencil'
                    user_font_size: '48sp'
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    theme_text_color: "Custom"
                    text_color: 1, 1, 1, 1
                    on_release: app.change_screen('edit')
                MDIconButton:
                    icon: 'cog-outline'
                    user_font_size: '48sp'
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    theme_text_color: "Custom"
                    text_color: 1, 1, 1, 1
                    on_release: app.change_screen('setting')

"""
print(KV)

class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        self.screen = Builder.load_string(KV)
        return self.screen

    def change_screen(self, screen_name):
        self.root.ids.screen_manager.current = screen_name
    

    



    def update_label(self):
        try:
            # Retrieve the ScreenManager instance
            screen_manager = self.root.ids.screen_manager
            # Access the SearchScreen
            search_screen = screen_manager.get_screen('search')
            # Retrieve the user's input and update the label
            user_input = search_screen.ids.user_input.text
            search_screen.ids.label.text = user_input
        except AttributeError as e:
            print(f"AttributeError: {e} - Make sure all IDs are correctly defined.")
        except Exception as e:
            print(f"An error occurred: {e}")




    def print_text(self):
        def process_inputs(inp_):
            print(inp_)
            dt = DataBase.dt
            liste = []

            columns = [
                "Full_name_of_the_employee",
                "Phone_number",
                "Date",
                "Type_of_car",
                "Description",
                "Been_worked_on"
            ]

            for column in columns:
                if inp_:
                    result = dt.search_database_by_prefix(column, inp_)
                    if result:
                        liste.append(result)

            if not liste:
                return None

            return '\n'.join(liste)

        # Accessing all text fields and the output label
        inp = self.root.ids.input1.text
        output_label = self.root.ids.output_label
        text_box = self.root.ids.text_box
        scroll_view = self.root.ids.scroll_view
        dt = DataBase.dt

        # Update the text and height of the label
        if not inp:
            output_label.text = dt.display_all_data()
        else:
            output_label.text = process_inputs(inp)
        output_label.height = output_label.texture_size[1]

        # Update the height of the MDBoxLayout to fit the content
        text_box.height = output_label.height + sum([child.height for child in text_box.children if child != output_label])

        # Scroll to the bottom of the ScrollView
        scroll_view.scroll_y = 0





MainApp().run()
