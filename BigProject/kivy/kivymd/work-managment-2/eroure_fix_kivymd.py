from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.metrics import dp


def print_widget_info(self, widget, indent=0):
        indent_space = ' ' * indent

        widget_id = getattr(widget, 'id', 'No ID')
        widget_text = getattr(widget, 'text', 'No Text')

        if isinstance(widget, MDTextField):
            print(f"{indent_space}MDTextField (id={widget_id}): {widget_text}")
        elif isinstance(widget, MDLabel):
            print(f"{indent_space}MDLabel (id={widget_id}): {widget_text}")
        elif isinstance(widget, (MDBoxLayout, BoxLayout, GridLayout)):
            print(f"{indent_space}{widget.__class__.__name__} (id={widget_id}):")
            for child in widget.children:
                self.print_widget_info(child, indent + 4)
        else:
            print(f"{indent_space}{widget.__class__.__name__} (id={widget_id})")


def sss(self):
    screen_manager = self.root.ids.screen_manager
    for screen_name in screen_manager.screen_names:
        screen = screen_manager.get_screen(screen_name)
        print(f"Screen name: {screen_name}")
        print(f"Screen content: {screen}")

        if hasattr(screen, 'children'):
            for widget in screen.children:
                self.print_widget_info(widget)
        else:
            print(f"Screen {screen_name} does not have children")
        print("------")
