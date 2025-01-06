from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
from kivy.uix.scrollview import ScrollView
from kivy.metrics import dp

class CreateProfileScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Load the screen's layout
        self.add_widget(Builder.load_string('''
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
                            on_release: app.print_text()
            '''))

class SearchScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Load the screen's layout
        self.add_widget(Builder.load_string('''
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
            '''))

# Define other screens similarly...
