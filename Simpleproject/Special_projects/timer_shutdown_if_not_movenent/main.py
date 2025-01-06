from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.core.window import Window
import founction


class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        button = Button(text='start', font_size=15, size_hint=(None, None), size=(300, 150),
                        pos_hint={'center_x': 0.5, 'center_y': 0.5},
                        background_color=(0, 0, 0, 0.95))


        def on_button_click(instance):
            instance.background_color = (0, 0, 0, 0.8)
            Clock.schedule_once(lambda dt: setattr(instance,'background_color', (0, 0, 0, 0.93)), 2)
            Clock.schedule_once(founction.main, 5)



        button.bind(on_press=on_button_click)
        layout.add_widget(button)

        exit_button = Button(text='Exit', size_hint=(None, None), size=(200, 100),pos_hint={'center_x': 0.5, 'center_y': 0.1},
                        background_color=(0, 0, 0, 0.8))
        exit_button.bind(on_press=self.stop)
        layout.add_widget(exit_button)

        return layout


Window.clearcolor = (0.2, 0.3, 0, 0.7)

if __name__ == '__main__':
    MyApp().run()
