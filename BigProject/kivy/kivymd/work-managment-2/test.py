from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.list import TwoLineIconListItem, IconLeftWidget
from kivy.metrics import dp

KV = """
ScreenManager:
    MainScreen:

<MainScreen>:
    name: 'main'
    BoxLayout:
        orientation: 'vertical'

        ScrollView:
            do_scroll_x: False
            do_scroll_y: True

            MDBoxLayout:
                id: items_box
                orientation: 'vertical'
                size_hint_y: None
                height: self.minimum_height
                padding: dp(20)
                spacing: dp(10)

        MDCard:
            size_hint_y: None
            height: dp(50)
            elevation: 10
            md_bg_color: app.theme_cls.primary_color
            padding: dp(10)
            radius: [0, 0, 25, 25]
            MDRaisedButton:
                text: 'Add Item'
                pos_hint: {'center_x': 0.5}
                on_release: root.add_item()
"""

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.item_counter = 1  

    def add_item(self):
        item_text = f"Item {self.item_counter}"
        self.item_counter += 1

        new_item = TwoLineIconListItem(
            text=item_text,
            secondary_text="Description"
        )
        new_item.add_widget(IconLeftWidget(icon='plus'))
        self.ids.items_box.add_widget(new_item)
        self.ids.items_box.height = self.ids.items_box.minimum_height

class MyApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

MyApp().run()
