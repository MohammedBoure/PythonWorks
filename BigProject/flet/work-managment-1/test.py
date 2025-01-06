import flet as ft

# قائمة البيانات لمحاكاة قاعدة بيانات
data_list = ["omar", "zinab", "khaled", "mohamad","omar", "zinab", "khaled", "mohamad","omar", "zinab", "khaled", "mohamad"]

# تعريف المتغيرات
search_field = None
data_table = None

def search_database(query):
    return [item for item in data_list if query.lower() in item.lower()]


def on_check_change(e):
    item = e.control.data
    if e.control.value: 
        handle_item_selected(item)
    else:
        handle_item_deselected(item)

def handle_item_selected(item):
    print(f"Item selected: {item}")

def handle_item_deselected(item):
    print(f"Item deselected: {item}")

def on_search(e):
    input_value = search_field.value

    data_table.rows.clear()

    results = search_database(input_value)

    for item in results:

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
    
    e.page.update()

def search_page(page):
    global search_field, data_table
    page.scroll = ft.ScrollMode.AUTO
    search_field = ft.TextField(
        label="Search", 
        bgcolor=ft.colors.WHITE,
    )
    
    data_table = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Data", color=ft.colors.BLUE)), 
            ft.DataColumn(ft.Text("Select", color=ft.colors.BLUE)) 
        ],
        rows=[],
    )
    

    page.add(
        ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text("Search Page", color=ft.colors.BLUE, size=24),  
                    search_field,
                    ft.ElevatedButton(
                        text="Search", 
                        bgcolor=ft.colors.BLUE, 
                        color=ft.colors.WHITE, 
                        on_click=on_search
                    ),
                    ft.Container(
                        content=data_table,
                        width=None,  
                        height=None,  
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=10,
            ),
            padding=10,
            bgcolor=ft.colors.BLACK,
            width=None, 
        )
    )


