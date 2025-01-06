from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
import DataBase

KV = '''
MDScreen:
    MDBoxLayout:
        orientation: 'vertical'
        padding: 20
        spacing: 20

        ScrollView:
            id: scroll_view
            do_scroll_x: False
            do_scroll_y: True
            MDBoxLayout:
                id: text_box
                orientation: 'vertical'
                size_hint_y: None
                height: self.minimum_height

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

                MDRaisedButton:
                    text: 'Press for submit'
                    pos_hint: {'center_x': 0.5}
                    on_release: app.print_text()

                MDLabel:
                    id: output_label
                    text: 'This place for text'
                    halign: 'center'
                    theme_text_color: 'Primary'
                    size_hint_y: None
                    height: self.texture_size[1]
'''

class MainScreen(Screen):
    pass

class MyApp(MDApp):
    def build(self):
        self.screen = Builder.load_string(KV)
        return self.screen

    def print_text(self):
        def process_inputs(inp1, inp2, inp3, inp4, inp5, inp6):          
            dt = DataBase.dt
            liste = []

            # Define the columns and inputs
            columns = [
                ("Full_name_of_the_employee", inp1),
                ("Phone_number", inp2),
                ("Date", inp3),
                ("Type_of_car", inp4),
                ("Description", inp5),
                ("Been_worked_on", inp6)
            ]

            # Loop through columns and inputs
            for column, inp in columns:
                if inp:
                    # Search the database with each non-empty input
                    result = dt.search_database_by_prefix(column, inp)
                    if result:  # Check if the result is not empty
                        liste.append(result)

            # If no inputs match, return None or empty string
            if not liste:
                return None  # or return "" if you prefer an empty string

            # Return combined results
            return '\n'.join(liste)


        # Accessing all text fields and the output label
        inp1 = self.screen.ids.input1.text
        inp2 = self.screen.ids.input2.text
        inp3 = self.screen.ids.input3.text
        inp4 = self.screen.ids.input4.text
        inp5 = self.screen.ids.input5.text
        inp6 = self.screen.ids.input6.text

        output_label = self.screen.ids.output_label
        text_box = self.screen.ids.text_box
        scroll_view = self.screen.ids.scroll_view
        dt = DataBase.dt
        # Update the text and height of the label
        if not inp1 and not inp2 and not inp3 and not inp4 and not inp5 and not inp6:
            output_label.text = dt.display_all_data()
        else:
            output_label.text = process_inputs(inp1,inp2,inp3,inp4,inp5,inp6)
        output_label.height = output_label.texture_size[1]

        # Update the height of the MDBoxLayout to fit the content
        text_box.height = output_label.height + sum([child.height for child in text_box.children if child != output_label])

        # Scroll to the bottom of the ScrollView
        scroll_view.scroll_y = 0

MyApp().run()
