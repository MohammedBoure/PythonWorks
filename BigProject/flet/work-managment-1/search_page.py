import flet as ft
import DataBase

ITEMS_PER_PAGE = 6  # عرض 6 عناصر بدلاً من 8
all_results = []
current_index = 0

def on_check_change(e):
    item = e.control.data
    if e.control.value:
        handle_item_selected(item)
    else:
        handle_item_deselected(item)

def handle_item_selected(item):
    if "yes" in item:
        print(f"Item selected: {item.split('|')}")
    else:
        print(111)

def handle_item_deselected(item):
    print(f"Item deselected: {item}")

def on_search(e):
    global all_results, current_index
    input_value = search_field.value
    try:
        print(f"Searching for: {input_value}")  # طباعة قيمة البحث
        all_results = DataBase.process_input(input_value)
        print(f"Results found: {len(all_results)}")  # طباعة عدد النتائج
        current_index = 0
        update_data_table(e.page)
        e.page.update()
    except Exception as ex:
        print(f"Error during search: {ex}")

def update_data_table(page):
    global current_index
    data_table.rows.clear()
    end_index = min(current_index + ITEMS_PER_PAGE, len(all_results))
    print(f"Loading data from index {current_index} to {end_index}")  # تأكيد البيانات التي يتم تحميلها
    for item in all_results[current_index:end_index]:
        new_row = ft.DataRow(
            cells=[
                ft.DataCell(ft.Text(item, color=ft.colors.GREEN)),
                ft.DataCell(ft.Checkbox(
                    value=False,
                    on_change=on_check_change,
                    data=item
                ))
            ]
        )
        data_table.rows.append(new_row)
    current_index = end_index

    if current_index >= len(all_results):
        load_more_button.visible = False
        print("No more data to load. Hiding button.")
    else:
        load_more_button.visible = True
        print("More data available. Showing button.")
    
    page.update()

def show_more_data(e):
    print("Load More button clicked.")  # تأكيد أن الزر ينفذ الدالة
    update_data_table(e.page)
    print(f"Button visible after click: {load_more_button.visible}")  # تأكيد حالة الزر بعد الضغط
    e.page.update()

def show_previous_data(e):
    global current_index
    if current_index - ITEMS_PER_PAGE >= 0:
        current_index -= ITEMS_PER_PAGE
        update_data_table(e.page)
    print("Previous button clicked.")  # تأكيد أن الزر ينفذ الدالة
    print(f"Button visible after click: {load_more_button.visible}")  # تأكيد حالة الزر بعد الضغط
    e.page.update()

def search_page(page):
    global search_field, data_table, load_more_button, previous_button
    
    search_field = ft.TextField(
        label="بحث",
        bgcolor="#000000B3",  # لون خلفية الحقل مع شفافية
        color=ft.colors.WHITE,
        text_align=ft.TextAlign.RIGHT,
        width=200,
        border_color=ft.colors.WHITE
    )
    
    data_table = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("البيانات", color=ft.colors.WHITE)),
            ft.DataColumn(ft.Text("اختيار", color=ft.colors.WHITE))
        ],
        rows=[]
    )
    
    load_more_button = ft.ElevatedButton(
        text="تحميل المزيد",
        bgcolor="#b7e4c7",
        color=ft.colors.WHITE,
        on_click=show_more_data,
        elevation=8,  # إضافة ظل للزر
        width=150,  # عرض ثابت للزر
        height=40  # ارتفاع ثابت للزر
    )
    
    previous_button = ft.ElevatedButton(
        text="سابق",
        bgcolor="#b7e4c7",
        color=ft.colors.WHITE,
        on_click=show_previous_data,
        elevation=8,  # إضافة ظل للزر
        width=150,  # عرض ثابت للزر
        height=40  # ارتفاع ثابت للزر
    )
    
    buttons_row = ft.Row(
        controls=[
            previous_button,
            ft.Container(width=10),  # إضافة مسافة بين الأزرار
            load_more_button
        ],
        alignment=ft.MainAxisAlignment.CENTER,  # توسيط الأزرار في الصف
        spacing=10  # المسافة بين الأزرار
    )
    
    return ft.Container(
        content=ft.Column(
            controls=[
                search_field,
                buttons_row,  # وضع الأزرار تحت حقل الإدخال
                ft.ElevatedButton(
                    text="بحث",
                    bgcolor="#b7e4c7",
                    color=ft.colors.WHITE,
                    on_click=on_search,
                    elevation=8,  # إضافة ظل للزر
                    width=300,  # عرض ثابت للزر
                    height=40  # ارتفاع ثابت للزر
                ),
                ft.Container(
                    content=data_table,
                    width=800,  # عرض ثابت للجدول
                    height=400,
                    margin=ft.margin.only(top=20),
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=10
        ),
        padding=ft.padding.only(top=50, bottom=10, left=10, right=10),  # إضافة هامش علوي للصفحة
        bgcolor="#000000B3",  # لون الخلفية مع شفافية
        height=600
    )
