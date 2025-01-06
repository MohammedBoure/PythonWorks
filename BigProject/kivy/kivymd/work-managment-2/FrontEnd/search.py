code = """

<SearchScreen>:
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

"""