from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.theming import ThemeManager
import MDFiles.MS as MS

Window.size = (360, 640)


KV = MS.code

class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"  
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_string(KV)

    def change_screen(self, screen_name):
        self.root.ids.screen_manager.current = screen_name

MainApp().run()
