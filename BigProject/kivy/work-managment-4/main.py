from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.popup import Popup


from fonts import register_fonts
from popup_functions import show_popup_1, show_popup_2, show_popup_3, show_popup_4,info

from utils import arabic, convert_string_to_list,serch_in_list

from client import Create_and_add_clients_data,remove_data_in_db_client
import DataBase



register_fonts()

class ContactList(BoxLayout):
    """
        Initializes the ContactList class, which is the main layout for the app. It sets up the interface for
        managing contact information, including buttons for interacting with popups, a form for adding contacts,
        and a scrollable view for displaying the list of contacts. It also loads existing contact data from 
        the database when the app starts.
    """
    def __init__(self, **kwargs):
        self.client = DataBase.DataHandling("clients.db")
        self.metal = DataBase.DataHandling("metal.db")
        
        self.list_metal = []
        self.list_client = []
        self.list_client_all = []
        self.list_metal_all = []
        self.relaod_data_client()
        self.relaod_data_metal()
        
        super().__init__(**kwargs)
        self.orientation = 'vertical'

        screen_width, screen_height = Window.size  # الحصول على أبعاد الشاشة

        self.top_button_layout = BoxLayout(size_hint_y=None, height=screen_height * 0.08, padding=[10, 10, 10, 10], spacing=10)
        
        for i in range(1, 5):
            btn_text = ""
            if i == 1:
                btn_text = arabic("إضافة منتج")
            elif i == 2:
                btn_text = arabic("إزالة منتج")
            elif i == 3:
                btn_text = arabic("البحث")
            else:
                btn_text = arabic(f"زر {i}")
            
            # استخدام size_hint بدلاً من الحجم الثابت
            btn = Button(text=btn_text, size_hint=(0.25, 1), font_name='ArabicFont')
            btn.bind(on_press=self.get_popup_function(i))
            self.top_button_layout.add_widget(btn)

        # محتوى الصفحة الرئيسي
        self.main_content_layout = BoxLayout(orientation='vertical', spacing=10, padding=[10, 0, 10, 10])

      
        input_height = screen_height * 0.05  # تعيين ارتفاع يعتمد على نسبة من ارتفاع الشاشة
        
        self.dimensions_of_metal = Spinner(
            text=arabic("dim"),
            values=self.list_metal,
            size_hint_y=None,
            height=input_height,
            font_name='ArabicFont'
        )
        self.full_name = TextInput(
            hint_text=arabic("الإسم و اللقب"), multiline=False,
            size_hint_y=None, height=input_height, font_name='ArabicFont'
        )
        self.Number_of_phone = TextInput(
            hint_text=arabic("رقم الهاتف"), multiline=False,
            size_hint_y=None, height=input_height, font_name='ArabicFont'
        )
        self.Number_of_items = TextInput(
            hint_text=arabic("عدد العناصر"), multiline=False,
            size_hint_y=None, height=input_height, font_name='ArabicFont'
        )
        self.date = TextInput(
            hint_text=arabic("التاريخ"), multiline=False,
            size_hint_y=None, height=input_height, font_name='ArabicFont'
        )
        self.price_has_been_paid = Spinner(
            text=arabic("الدفع"),
            values=["yes", "no"],
            size_hint_y=None,
            height=input_height,
            font_name='ArabicFont'
        )
        self.Comment = TextInput(
            hint_text=arabic("تعليق"), multiline=False,
            size_hint_y=None, height=input_height, font_name='ArabicFont'
        )
        self.entre = Button(
            text=arabic("أدخل"),
            on_press=self.add_contact,
            size_hint_y=None,
            height=screen_height * 0.08,  # حجم أكبر بناءً على الشاشة
            font_name='ArabicFont'
        )
        
        # إضافة ScrollView لتناسب الحقول
        self.scroll_view = ScrollView(size_hint=(1, 1), size=(screen_width, screen_height * 0.5))
        self.contact_labels = GridLayout(cols=1, size_hint_y=None)
        self.contact_labels.bind(minimum_height=self.contact_labels.setter('height'))
        self.scroll_view.add_widget(self.contact_labels)

        # إضافة العناصر إلى التخطيط الرئيسي
        self.main_content_layout.add_widget(self.dimensions_of_metal)
        self.main_content_layout.add_widget(self.full_name)
        self.main_content_layout.add_widget(self.Number_of_phone)
        self.main_content_layout.add_widget(self.Number_of_items)
        self.main_content_layout.add_widget(self.date)
        self.main_content_layout.add_widget(self.price_has_been_paid)
        self.main_content_layout.add_widget(self.Comment)
        self.main_content_layout.add_widget(self.entre)
        self.main_content_layout.add_widget(self.scroll_view)

        # إضافة التخطيطات إلى الواجهة
        self.add_widget(self.top_button_layout)
        self.add_widget(self.main_content_layout)

        self.current_contact_box = None  
        self.load_contacts_from_database()
        
    def relaod_data_client(self):
        self.list_client_all = convert_string_to_list(self.client.display_all_data("Clients"))
        
        if len(self.list_client_all[0]) == 1:
            self.list_client = []
        else:
            self.list_client = self.list_client_all[1:]
            
    def relaod_data_metal(self):
        self.list_metal_all = convert_string_to_list(self.metal.display_all_data("Metal"))

        if len(self.list_metal_all[0]) == 1:
            self.list_metal = []
        else:
            self.list_metal = []
            for _ in self.list_metal_all:
                self.list_metal.append(_[1])
            self.list_metal = self.list_metal[1:]
        
    """
        Loads the existing contact information from the database and displays it in the scrollable contact list.
        This method retrieves data from the database and creates a visual representation of each contact using
        a BoxLayout that contains a Label and buttons for editing or deleting each contact.
    """
    def load_contacts_from_database(self): 
        for contact in self.list_client:
            if len(contact)>=6:
                self.num = contact[0]
                self.dimensions_of_metal.text = contact[1]
                self.full_name.text = contact[2]
                self.Number_of_phone.text = contact[3]
                self.Number_of_items.text =contact[4]
                self.date.text = contact[5]
                self.price_has_been_paid.text =contact[6]
                self.Comment.text = contact[7]
                self.add_contact_first()           

    """
        Returns the appropriate popup function for each button based on its number. This function maps 
        button numbers (1-4) to their corresponding popup display functions (show_popup_1, show_popup_2, etc.)
        to display a specific popup when the button is pressed.
        
        :param button_number: The number of the button (1, 2, 3, or 4) which determines which popup function to call.
        :return: A function wrapper that triggers the appropriate popup function when a button is pressed.
    """
    def get_popup_function(self, button_number):
        def wrapper(instance):
            popup_functions = {
                1: show_popup_1,
                2: lambda: show_popup_2(self.list_metal_all), 
                3: show_popup_3,
                4: show_popup_4
            }
            popup_function = popup_functions.get(button_number, lambda: None)
            popup_function()

        return wrapper

    """
        Adds a new contact to the database and the UI. This method is triggered when the 'Enter' button is pressed.
        It collects user input from the form fields (like name, phone number, etc.), saves the contact in the database,
        and updates the UI with the new contact's information. It also clears the form fields after adding the contact.
        
        :param instance: The button instance that triggered this function.
    """
    def add_contact(self, interface):
        self.relaod_data_client()
        try:
            num = int(self.list_client_all[-1][0]) + 1
        except:
            num = 1

        dim = self.dimensions_of_metal.text  
        full_name = self.full_name.text  
        Number_phone = self.Number_of_phone.text  
        Number_of_items = self.Number_of_items.text  
        Date = self.date.text  
        Price_has_been_paid = self.price_has_been_paid.text 
        Comment = self.Comment.text

        bol = serch_in_list([num, dim, full_name, Number_phone, Number_of_items, Date, Price_has_been_paid, Comment], self.list_client)

        if dim and full_name and Number_phone and Number_of_items and Date and Price_has_been_paid and Comment and not bol:
            if not serch_in_list([num, dim, full_name, Number_phone, Number_of_items, Date, Price_has_been_paid, Comment], self.list_client):
                Create_and_add_clients_data(dim, full_name, Number_phone, Number_of_items, Date, Price_has_been_paid, Comment)

            # ضبط المحتويات داخل BoxLayout تلقائيًا
            contact_box = BoxLayout(size_hint_y=None, height=60)  # يمكن تغيير الارتفاع أو جعلها متكيفة
            label_text = f"{num}  {dim}   {full_name}"
            label = Label(text=arabic(label_text), size_hint=(.6, 1), font_name='ArabicFont')

            # أزرار التفاعل (حذف، تعديل، معلومات)
            remove_button = Button(
                text=arabic("حذف"), 
                on_press=lambda x: self.confirm_remove(contact_box), 
                size_hint=(.2, 1), 
                font_name='ArabicFont'
            )
            edit_button = Button(
                text=arabic("تعديل"), 
                size_hint=(.2, 1), 
                font_name='ArabicFont', 
                on_press=lambda x: self.edit_contact(num, dim, full_name, Number_phone, Number_of_items, Date, Price_has_been_paid, Comment, contact_box)
            )
            info_button = Button(
                text=arabic("معلومات"), 
                on_press=lambda x: info(num), 
                size_hint=(.2, 1), 
                font_name='ArabicFont'
            )

            # إضافة المكونات إلى BoxLayout
            contact_box.add_widget(label)
            contact_box.add_widget(remove_button)
            contact_box.add_widget(edit_button)
            contact_box.add_widget(info_button)

            # إضافة contact_box إلى القائمة
            self.contact_labels.add_widget(contact_box)

            # تفريغ المدخلات بعد الإضافة
            self.clear_inputs()

            
    def add_contact_first(self):
        try:
            num = self.num
        except:
            num = 1
        
        dim = self.dimensions_of_metal.text  
        full_name = self.full_name.text  
        Number_phone = self.Number_of_phone.text  
        Number_of_items = self.Number_of_items.text  
        Date = self.date.text  
        Price_has_been_paid = self.price_has_been_paid.text  
        Comment = self.Comment.text

        # التأكد من أن جميع الحقول ممتلئة قبل إضافة الاتصال
        if dim and full_name and Number_phone and Number_of_items and Date and Price_has_been_paid and Comment:
            
            # BoxLayout للحفاظ على تنسيق العرض
            contact_box = BoxLayout(size_hint_y=None, height=60)
            label_text = f"{num}  {dim}   {full_name}"
            
            # إضافة المكونات
            label = Label(text=label_text, size_hint=(.6, 1))

            # زر الحذف
            remove_button = Button(
                text=arabic("حذف"), 
                on_press=lambda x: self.confirm_remove(contact_box), 
                size_hint=(.2, 1), 
                font_name='ArabicFont'
            )

            # زر التعديل
            edit_button = Button(
                text=arabic("تعديل"), 
                size_hint=(.2, 1), 
                font_name='ArabicFont', 
                on_press=lambda x: self.edit_contact(num, dim, full_name, Number_phone, Number_of_items, Date, Price_has_been_paid, Comment, contact_box)
            )

            # زر المعلومات
            info_button = Button(
                text=arabic("معلومات"), 
                on_press=lambda x: info(num), 
                size_hint=(.2, 1), 
                font_name='ArabicFont'
            )

            # إضافة المكونات إلى BoxLayout
            contact_box.add_widget(label)
            contact_box.add_widget(remove_button)
            contact_box.add_widget(edit_button)
            contact_box.add_widget(info_button)

            # إضافة contact_box إلى واجهة الاتصال
            self.contact_labels.add_widget(contact_box)

            # تفريغ المدخلات بعد إضافة الاتصال
            self.clear_inputs()
    """
        Loads the selected contact's details into the input fields for editing. When the user selects 'Edit', this method
        is called to pre-fill the input fields with the contact's current information, allowing the user to update the data.
        It also modifies the behavior of the 'Enter' button to act as an 'Update' button for saving changes.
        
        :param dim: The dimension or self.metal type of the contact.
        :param full_name: The full name of the contact.
        :param num_phone: The phone number of the contact.
        :param num_items: The number of items associated with the contact.
        :param date: The date associated with the contact.
        :param prix: The price paid by the contact.
        :param contact_box: The UI element representing the contact in the contact list.
    """     
    def edit_contact(self,num, dim, full_name, num_phone, num_items, date, prix,Comment, contact_box):
        self.num = num
        self.dimensions_of_metal.text = dim
        self.full_name.text = full_name
        self.Number_of_phone.text = num_phone
        self.Number_of_items.text = num_items
        self.date.text = date
        self.price_has_been_paid.text = prix 
        self.Comment.text = Comment
        
        label = contact_box.children[2]  
        label_text = label.text  

        self.current_contact_box = contact_box
        self.entre.text = arabic("تحديث المعلومات ")
        self.entre.unbind(on_press=self.add_contact) 
        self.entre.bind(on_press=self.update_contact)

    """
        Updates the contact's information in the UI after the user has edited it. This method is triggered when the
        'Update' button is pressed. It retrieves the modified data from the input fields, updates the corresponding
        contact's details in the UI, and restores the 'Enter' button to its original function after the update is complete.
        
        :param instance: The button instance that triggered this function.
    """
    def update_contact(self, instance):
        new_num = self.num
        new_dim = self.dimensions_of_metal.text
        new_full_name = self.full_name.text
        new_Number_phone = self.Number_of_phone.text
        new_Number_of_items = self.Number_of_items.text
        new_Date = self.date.text
        new_Price_has_been_paid = self.price_has_been_paid.text
        new_Comment = self.Comment.text
        
        remove_data_in_db_client(new_num)
        Create_and_add_clients_data(new_dim,new_full_name,new_Number_phone,new_Number_of_items,new_Date,new_Price_has_been_paid,new_Comment)
        label_text = f"{new_num}  {new_dim}   {new_full_name}"
        
        x = 0
        for widget in self.current_contact_box.children:
            x += 1
            if isinstance(widget, Label) and x == 4:
                widget.text = label_text
                break 

        self.reset_enter_button()

        self.clear_inputs()
        self.current_contact_box = None

    """
        Resets the 'Enter' button to its original state after updating a contact. This method is called to rebind the 
        button back to the 'add_contact' function and change its label back to 'Enter' after an edit operation is complete.
    """
    def reset_enter_button(self):
        self.entre.text = arabic("أدخل")  
        self.entre.unbind(on_press=self.update_contact) 
        self.entre.bind(on_press=self.add_contact)  

    """
        Opens a confirmation popup when the user presses the 'Remove' button for a contact. This method creates a popup
        window with a confirmation message asking the user if they are sure they want to delete the contact. The popup
        contains two buttons: one to confirm and delete the contact, and one to cancel the deletion.
        
        :param contact_box: The UI element representing the contact that the user wants to delete.
    """
    def confirm_remove(self, contact_box):
        label = contact_box.children[3]  
        label_text = label.text  

        content = BoxLayout(orientation='vertical')

        content.add_widget(Label(text=arabic("هل أنت متأكد من حذف هذه الجهة؟"), size_hint_y=None, height=80, font_name='ArabicFont'))

        label_to_show = Label(text=label_text, size_hint_y=None, height=80, font_name='ArabicFont')
        content.add_widget(label_to_show)

        yes_button = Button(text=arabic("نعم"), size_hint_y=None, height=100, font_name='ArabicFont')
        no_button = Button(text=arabic("لا"), size_hint_y=None, height=100, font_name='ArabicFont')

        content.add_widget(yes_button)
        content.add_widget(no_button)

        popup = Popup(title=arabic("تأكيد"), content=content, size_hint=(0.8, 0.5))

        def on_yes_press(instance):
            remove_data_in_db_client(label_text)
            remove_data_in_db_client(label_text)
            self.remove_contact(contact_box)
            popup.dismiss()

        yes_button.bind(on_press=on_yes_press)
        no_button.bind(on_press=popup.dismiss)

        popup.open()

    """
        Removes a contact from the UI. This method is called when the user confirms they want to delete a contact.
        It removes the contact's UI element (contact_box) from the scrollable list of contacts.
        
        :param contact_box: The UI element representing the contact that will be removed.
    """
    def remove_contact(self, contact_box):
        if contact_box in self.contact_labels.children:
            self.contact_labels.remove_widget(contact_box)

    """
        Clears all input fields in the form. This method is used to reset the text fields for adding or editing contacts
        after a contact has been added or updated, ensuring that the fields are empty and ready for the next operation.
    """
    def clear_inputs(self):
        self.dimensions_of_metal.text = ''
        self.full_name.text = ''
        self.Number_of_phone.text = ''
        self.Number_of_items.text = ''
        self.date.text = ''
        self.price_has_been_paid.text = ''
        self.Comment.text = ''
    
class MyApp(App):
    def build(self):
        return ContactList()

if __name__ == '__main__':
    MyApp().run()
