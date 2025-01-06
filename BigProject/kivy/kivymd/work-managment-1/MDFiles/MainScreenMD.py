code = '''
<MainScreen>:
    BoxLayout:
        orientation: 'vertical'

        MDTopAppBar:
            title: "Main Screen"
            elevation: 10

        BoxLayout:
            orientation: 'vertical'
            spacing: 20
            padding: 20

            MDRaisedButton:
                text: "create profile"
                size_hint: (1, 0.3)
                on_release: app.change_screen("input_screen")

            MDRaisedButton:
                text: "Go to Page 2"
                size_hint: (1, 0.3)
                on_release: app.change_screen("screen2")

            MDRaisedButton:
                text: "Go to Page 3"
                size_hint: (1, 0.3)
                on_release: app.change_screen("screen3")

'''