from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.core.text import LabelBase
from kivy.uix.popup import Popup
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.metrics import dp

from utils import arabic,relaod_of_data_metal
from fonts import register_fonts
from metal import Create_and_add_metal_data,remove_data_in_db_metal
import DataBase
from kivy.core.clipboard import Clipboard


dt = DataBase.DataHandling("clients.db")

register_fonts()
def show_popup_1():
    content = BoxLayout(orientation='vertical', padding=[10, 10, 10, 10], spacing=10)

    label = Label(text=arabic("أدخل البيانات التي تود إضافتها"),
                  size_hint_y=None, 
                  height=dp(40), 
                  font_name='ArabicFont')
    
    content.add_widget(label)

    dim = TextInput(hint_text=arabic("الأبعاد"), 
                    multiline=False, 
                    size_hint=(1, None), 
                    height=dp(40), 
                    font_name='ArabicFont')
    
    num_ex = TextInput(hint_text=arabic("العناصر الموجودة"), 
                       multiline=False, 
                       size_hint=(1, None), 
                       height=dp(40), 
                       font_name='ArabicFont')
    
    num_used = TextInput(hint_text=arabic("العناصر المستغلة"), 
                         multiline=False, 
                         size_hint=(1, None), 
                         height=dp(40), 
                         font_name='ArabicFont')
    
    prix = TextInput(hint_text=arabic("سعر الكراء ليوم واحد"), 
                     multiline=False, 
                     size_hint=(1, None), 
                     height=dp(40), 
                     font_name='ArabicFont')

    entre = Button(text=arabic("أدخل"), 
                   on_press=lambda instance: Create_and_add_metal_data(dim.text, num_ex.text, num_used.text, prix.text), 
                   size_hint=(1, None), 
                   height=dp(50), 
                   font_name='ArabicFont')

    content.add_widget(dim)
    content.add_widget(num_ex)
    content.add_widget(num_used)
    content.add_widget(prix)
    content.add_widget(entre)

    total_height = dp(40) + dp(40*4) + dp(50) + dp(40)  + dp(50)

    popup = Popup(title="", content=content, size_hint=(0.8, None), height=total_height)
    
    popup.open()


def show_popup_2(list_of_data):
    relaod_of_data_metal()

    def remove_contact(contact_box):
        if contact_box in content.children:  
            content.remove_widget(contact_box) 

    def remove(contact_box):
        if isinstance(contact_box.children[1], Label):
            remove_contact(contact_box)  
            remove_data_in_db_metal(contact_box.children[1].text)  

    scroll_view = ScrollView(size_hint=(1, None), do_scroll_x=False)  
    
    content = BoxLayout(orientation='vertical', spacing=10, padding=[10, 10, 10, 10], size_hint_y=None)
    content.add_widget(Label(text=arabic("P:السعر     NU:العدد المستخدم      NP:العدد الموجود       D:الأبعاد     N:رقم التعريف"), 
                             size_hint_y=None, height=40, font_name='ArabicFont'))

    content.bind(minimum_height=content.setter('height'))
    
    list_of_data = list_of_data[1:] 
    
    for data in list_of_data:
        num = data[0]
        Dimensions = data[1]
        Number_present = data[2]
        Number_used = data[3]
        Prix = data[4]
        
        contact_box = BoxLayout(size_hint_y=None, height=100, spacing=10)
        
        label_text = f"N: {num}    D: {Dimensions}    NP: {Number_present}     NU: {Number_used}    P: {Prix}"
        label = Label(text=label_text, size_hint=(.6, 1), halign="right", valign="middle")
        label.bind(size=label.setter('text_size'))
                
        remove_button = Button(
            text=arabic("حذف"),
            size_hint=(.2, 1),
            font_name='ArabicFont',
            on_press=lambda instance, box=contact_box: remove(box)
        )

        contact_box.add_widget(label)
        contact_box.add_widget(remove_button)
        
        content.add_widget(contact_box)
        
    scroll_view.add_widget(content)
    
    def adjust_popup_height(instance, value):
        max_height = 800
        new_height = min(content.height, max_height)
        scroll_view.height = new_height + 30
        popup.height = new_height + 200

    content.bind(height=adjust_popup_height)
    

    popup = Popup(title="Number   Dimensions   Number_present   Number_used    Prix", 
                  content=scroll_view, 
                  size_hint=(0.8, None))  
    
    popup.open()


   
def show_popup_3():
    def remove_contact(contact_box):
        if contact_box in content.children:  
            content.remove_widget(contact_box) 

    def remove(contact_box):
        if isinstance(contact_box.children[1], Label):
            remove_contact(contact_box)  
            remove_data_in_db_metal(contact_box.children[1].text)  

    scroll_view = ScrollView(size_hint=(1, None), do_scroll_x=False)  
    content = BoxLayout(orientation='vertical', spacing=10, padding=[10, 10, 10, 10], size_hint_y=None)

    # Adding header label
    content.add_widget(Label(text=arabic("A:رقم التعريف     B:المنتج      C:الإسم \n      D:رقم الهاتف     E:العدد المستخدم       F:التاريخ    G:تم العمل "),size_hint_y=None, height=80,font_name='ArabicFont'))

    content.bind(minimum_height=content.setter('height'))
    dt = DataBase.DataHandling("clients.db")
    
    input_data = TextInput(text=arabic(""), size_hint_y=None, height=80, font_name='ArabicFont')
    content.add_widget(input_data)

    def update_content(instance, text): 
        content.clear_widgets()
        content.add_widget(Label(text=arabic("A:رقم التعريف   B:النتج   C:الإسم   \n D:رقم الهاتف     E:العدد المستخدم    F:التاريخ    G:تم العمل "), 
                                 size_hint_y=None, height=80, font_name='ArabicFont'))
        content.add_widget(input_data) 
        
        list_of_data = dt.search_in_all_columns("Clients", input_data.text) 
        for data in list_of_data:
            a = data[0]
            b = data[1]
            c = data[2]
            d = data[3]
            e = data[4]
            f = data[5]
            g = data[6]

            contact_box = BoxLayout(size_hint_y=None, height=100, spacing=10)
            
            label_text = f"A:{a}     B:{b}     C:{c}    D:{d}    E:{e}    F:{f}    G:{g}"
            label = Label(text=label_text, size_hint=(.6, 1), halign="left", valign="middle")
            label.bind(size=label.setter('text_size'))

            contact_box.add_widget(label)
            content.add_widget(contact_box)

    input_data.bind(text=update_content)

    def adjust_popup_height(instance, value):
        max_height = 800
        new_height = min(content.height, max_height) 
        scroll_view.height = new_height + 30
        popup.height = new_height + 200
    
    content.bind(height=adjust_popup_height)
    
    scroll_view.add_widget(content) 
    popup = Popup(title=arabic(""), content=scroll_view, size_hint=(0.8, None), height=800)
    popup.open()


  
def show_popup_4():
    content = BoxLayout(orientation='vertical', spacing=10, padding=[10, 10, 10, 10], size_hint_y=None)
    content.bind(minimum_height=content.setter('height'))  
    content.add_widget(Label(text=arabic("هذه صفحة منبثقة 4"), size_hint_y=None, height=40, font_name='ArabicFont'))

    close_button = Button(text=arabic("إغلاق"), size_hint_y=None, height=50, font_name='ArabicFont')
    content.add_widget(close_button)


    popup = Popup(title="screen 4", content=content, size_hint=(0.8, None), height=400)  

    close_button.bind(on_press=popup.dismiss)
    
    def adjust_popup_height(instance, value):
        max_height = 400  
        new_height = min(content.height, max_height)  
        popup.height = new_height + 100

    content.bind(height=adjust_popup_height) 

    popup.open()



def info(text):
    def format_text(input_text):
        words = input_text.split()  
        formatted_text = ""
        
        for i in range(len(words)):
            formatted_text += words[i] + " "
            if (i + 1) % 5 == 0:
                formatted_text += "\n"
        
        return formatted_text.strip()

    if not isinstance(text, list):
        text = dt.selected_row("Clients", text)
    
    a = text[0]
    b = text[1]
    c = text[2]
    d = text[3]
    e = text[4]
    f = text[5]
    g = text[6]
    h = format_text(text[7])
    
    scroll_view = ScrollView(size_hint=(1, None), size=(400, 300), bar_width=10) 
    
    content = GridLayout(cols=2, padding=10, spacing=10, size_hint_y=None)
    content.bind(minimum_height=content.setter('height'))
    
    content.add_widget(Label(text=f"{a}", size_hint_y=None, height=30, font_size=18))
    content.add_widget(Label(text=arabic("رقم التعريف:"), size_hint_y=None, height=30, font_size=18, font_name='ArabicFont'))

    content.add_widget(Label(text=f"{b}", size_hint_y=None, height=30, font_size=18))
    content.add_widget(Label(text=arabic("المنتج:"), size_hint_y=None, height=30, font_size=18, font_name='ArabicFont'))

    content.add_widget(Label(text=f"{c}", size_hint_y=None, height=30, font_size=18))
    content.add_widget(Label(text=arabic("الإسم:"), size_hint_y=None, height=30, font_size=18, font_name='ArabicFont'))

    content.add_widget(Label(text=f"{d}", size_hint_y=None, height=30, font_size=18))
    
    d_button = Button(text=arabic('رقم الهاتف'), size_hint_x=None, height=30, width=100, font_size=18, font_name='ArabicFont')
    d_button.bind(on_press=lambda x: Clipboard.copy(d))
    content.add_widget(d_button)
        
    content.add_widget(Label(text=f"{e}", size_hint_y=None, height=30, font_size=18))
    content.add_widget(Label(text=arabic("العدد:"), size_hint_y=None, height=30, font_size=18, font_name='ArabicFont'))
    
    content.add_widget(Label(text=f"{f}", size_hint_y=None, height=30, font_size=18))
    content.add_widget(Label(text=arabic("التاريخ:"), size_hint_y=None, height=30, font_size=18, font_name='ArabicFont'))
    
    content.add_widget(Label(text=f"{g}", size_hint_y=None, height=30, font_size=18))
    content.add_widget(Label(text=arabic("الدفع:"), size_hint_y=None, height=30, font_size=18, font_name='ArabicFont'))

    h_box_layout = BoxLayout(orientation='vertical', size_hint_y=None, height=200)
    h_scroll_view = ScrollView(size_hint=(1, None), size=(400, 200), bar_width=10)
    
    h_label = Label(text=h, size_hint_y=None, height=len(h.split()) * 20, font_size=18, halign='left', valign='top')
    h_label.bind(size=h_label.setter('text_size'))  

    h_scroll_view.add_widget(h_label)
    h_box_layout.add_widget(h_scroll_view)
    
    content.add_widget(h_box_layout)
    
    content.add_widget(Label(text=arabic("تعليق:"), size_hint_y=None, height=30, font_size=18, font_name='ArabicFont'))
    
    scroll_view.add_widget(content)
    
    close_button = Button(text='exit', size_hint_y=None, height=40)
    close_button.bind(on_press=lambda x: popup.dismiss())
    
    layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
    layout.add_widget(scroll_view)
    layout.add_widget(close_button)
    
    def adjust_popup_height(instance, value):
        max_height = 600  
        new_height = min(content.height + 70, max_height)  
        scroll_view.height = new_height 
        popup.height = new_height + 70 
    
    content.bind(height=adjust_popup_height)
    
    popup = Popup(title='data', content=layout, size_hint=(0.8, None), height=600)  
    popup.open()

