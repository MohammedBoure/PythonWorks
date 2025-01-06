code = """

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



"""