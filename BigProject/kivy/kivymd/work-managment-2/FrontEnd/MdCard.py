code = """



        MDCard:
            size_hint_y: None
            height: dp(50)
            elevation: 10
            padding: dp(0)
            radius: [0, 0,25, 25]
            md_bg_color: app.theme_cls.bg_dark
            
            ScrollView:
                do_scroll_x: True
                do_scroll_y: False
                
                MDGridLayout:
                    cols: 5
                    adaptive_width: True
                    padding: dp(2)
                    spacing: dp(25)
                    

                    MDIconButton:
                        icon: 'file-plus'
                        user_font_size: '48sp'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        theme_text_color: "Custom"
                        text_color: 1, 1, 1, 1
                        on_release: app.change_screen('create_profile')
                    


                    MDIconButton:
                        icon: 'magnify'
                        user_font_size: '48sp'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        theme_text_color: "Custom"
                        text_color: 1, 1, 1, 1
                        on_release: app.change_screen('SearchScreen')
                    

                    MDIconButton:
                        icon: 'clock-outline'
                        user_font_size: '48sp'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        theme_text_color: "Custom"
                        text_color: 1, 1, 1, 1
                        on_release: app.change_screen('to_day_work')

                    MDIconButton:
                        icon: 'pencil'
                        user_font_size: '48sp'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        theme_text_color: "Custom"
                        text_color: 1, 1, 1, 1
                        on_release: app.change_screen('edit')
                    
                    MDIconButton:
                        icon: 'cog-outline'
                        user_font_size: '48sp'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        theme_text_color: "Custom"
                        text_color: 1, 1, 1, 1
                        on_release: app.change_screen('setting')
                        
"""