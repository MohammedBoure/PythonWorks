code = """

            MDScreen:
                name: 'setting'
                orientation: 'vertical'


                MDCard:
                    size_hint_y: None
                    height: dp(30)
                    elevation: 10
                    md_bg_color: app.theme_cls.primary_color
                    padding: dp(10)
                    radius: [0, 0, 25, 25]
                    MDLabel:
                        text: "setting"
                        halign: "center"
                        theme_text_color: "Custom"
                        text_color: 1, 1, 1, 1

            
"""