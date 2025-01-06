code = '''
<Screen3>:
    BoxLayout:
        orientation: 'vertical'
        padding: 20
        spacing: 20

        MDTopAppBar:
            title: "Page 3"
            elevation: 10

        BoxLayout:
            orientation: 'vertical'
            spacing: 20
            size_hint_y: None
            height: self.minimum_height

            MDLabel:
                id: label
                text: "This is Page 3"
                halign: 'center'

            MDRaisedButton:
                text: "Display Message"
                size_hint_y: None
                height: "56dp"
                pos_hint: {'center_x': 0.5}
                on_release: root.display_message()

            MDRaisedButton:
                text: "Back to Main"
                size_hint_y: None
                height: "56dp"
                pos_hint: {'center_x': 0.5}
                on_release: app.change_screen("main")


'''