code = '''
<Screen2>:
    BoxLayout:
        orientation: 'vertical'
        padding: 20
        spacing: 20

        MDTopAppBar:
            title: "Page 2"
            elevation: 10

        BoxLayout:
            orientation: 'vertical'
            spacing: 20
            size_hint_y: None
            height: self.minimum_height

            MDLabel:
                id: label
                text: "This is Page 2"
                halign: 'center'

            MDRaisedButton:
                text: "Change Color"
                size_hint_y: None
                height: "56dp"
                pos_hint: {'center_x': 0.5}
                on_release: root.change_color()

            MDRaisedButton:
                text: "Back to Main"
                size_hint_y: None
                height: "56dp"
                pos_hint: {'center_x': 0.5}
                on_release: app.change_screen("main")

'''