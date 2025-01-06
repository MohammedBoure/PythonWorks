
code = '''
MDScreen:

    BoxLayout:
        orientation: 'vertical'
        
        MDCard:
            size_hint_y: None
            height: dp(50)
            elevation: 10
            md_bg_color: app.theme_cls.primary_color
            padding: dp(10)
            radius: [0, 0, 25, 25]
            MDLabel:
                text: "My App"
                halign: "center"
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1
                
        ScreenManager:
            id: screen_manager

            MDScreen:
                name: 'home_screen'
                MDLabel:
                    text: 'Home Screen'
                    halign: 'center'
                    
            MDScreen:
                name: 'email_screen'
                MDLabel:
                    text: 'Email Screen'
                    halign: 'center'
                    
            MDScreen:
                name: 'account_screen'
                MDLabel:
                    text: 'Account Screen'
                    halign: 'center'
                    
            MDScreen:
                name: 'alarm_screen'
                MDLabel:
                    text: 'Alarm Screen'
                    halign: 'center'
                    
            MDScreen:
                name: 'calendar_screen'
                MDLabel:
                    text: 'Calendar Screen'
                    halign: 'center'
                    
            MDScreen:
                name: 'map_screen'
                MDLabel:
                    text: 'Map Screen'
                    halign: 'center'

        MDCard:
            size_hint_y: None
            height: dp(100)
            elevation: 10
            padding: dp(10)
            radius: [25, 25, 25, 25]
            md_bg_color: app.theme_cls.bg_dark
            
            ScrollView:
                do_scroll_x: True
                do_scroll_y: False
                
                MDGridLayout:
                    cols: 6
                    adaptive_width: True
                    padding: dp(10)
                    spacing: dp(10)
                    
                    MDCard:
                        size_hint: None, None
                        size: dp(70), dp(70)
                        elevation: 10
                        radius: [25, 25, 25, 25]
                        MDIconButton:
                            icon: 'home'
                            user_font_size: '48sp'
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            theme_text_color: "Custom"
                            text_color: 1, 1, 1, 1
                            on_release: app.change_screen('home_screen')
                    
                    MDCard:
                        size_hint: None, None
                        size: dp(70), dp(70)
                        elevation: 10
                        radius: [25, 25, 25, 25]
                        MDIconButton:
                            icon: 'email'
                            user_font_size: '48sp'
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            theme_text_color: "Custom"
                            text_color: 1, 1, 1, 1
                            on_release: app.change_screen('email_screen')
                    
                    MDCard:
                        size_hint: None, None
                        size: dp(70), dp(70)
                        elevation: 10
                        radius: [25, 25, 25, 25]
                        MDIconButton:
                            icon: 'account'
                            user_font_size: '48sp'
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            theme_text_color: "Custom"
                            text_color: 1, 1, 1, 1
                            on_release: app.change_screen('account_screen')
                    
                    MDCard:
                        size_hint: None, None
                        size: dp(70), dp(70)
                        elevation: 10
                        radius: [25, 25, 25, 25]
                        MDIconButton:
                            icon: 'alarm'
                            user_font_size: '48sp'
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            theme_text_color: "Custom"
                            text_color: 1, 1, 1, 1
                            on_release: app.change_screen('alarm_screen')
                    
                    MDCard:
                        size_hint: None, None
                        size: dp(70), dp(70)
                        elevation: 10
                        radius: [25, 25, 25, 25]
                        MDIconButton:
                            icon: 'calendar'
                            user_font_size: '48sp'
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            theme_text_color: "Custom"
                            text_color: 1, 1, 1, 1
                            on_release: app.change_screen('calendar_screen')
                    
                    MDCard:
                        size_hint: None, None
                        size: dp(70), dp(70)
                        elevation: 10
                        radius: [25, 25, 25, 25]
                        MDIconButton:
                            icon: 'map'
                            user_font_size: '48sp'
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            theme_text_color: "Custom"
                            text_color: 1, 1, 1, 1
                            on_release: app.change_screen('map_screen')
'''