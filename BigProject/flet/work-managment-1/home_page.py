import flet as ft
import DataBase

dt = DataBase.DataHandling("row")

def on_submit(e):
    print("Field 1:", field1.value)
    print("Field 2:", field2.value)
    print("Field 3:", field3.value)
    print("Field 4:", field4.value)
    print("Field 5:", field5.value)
    print("Field 6:", field6.value)
    print("Field 7:", field7.value)
    DataBase.insert_data_employees(
        field1.value,
        field2.value,
        field3.value,
        field4.value,
        field5.value,
        field6.value,
        field7.value,
    )

def home_page():
    global field1, field2, field3, field4, field5, field6, field7
    
    field_width = 250

    field1 = ft.TextField(
    bgcolor="#000000B3",
    color=ft.colors.WHITE,
    text_align=ft.TextAlign.RIGHT,
    width=field_width,
    border_color=ft.colors.WHITE
    )

    field2 = ft.TextField(
        bgcolor="#000000B3",
        color=ft.colors.WHITE,
        text_align=ft.TextAlign.RIGHT,
        width=field_width,
        border_color=ft.colors.WHITE
    )
    field3 = ft.TextField(
        bgcolor="#000000B3",
        color=ft.colors.WHITE,
        text_align=ft.TextAlign.RIGHT,
        width=field_width,
        border_color=ft.colors.WHITE
    )
    field4 = ft.TextField(
        bgcolor="#000000B3",
        color=ft.colors.WHITE,
        text_align=ft.TextAlign.RIGHT,
        width=field_width,
        border_color=ft.colors.WHITE
    )
    field5 = ft.TextField(
        bgcolor="#000000B3",
        color=ft.colors.WHITE,
        text_align=ft.TextAlign.RIGHT,
        width=field_width,
        border_color=ft.colors.WHITE
    )
    field6 = ft.TextField(
        bgcolor="#000000B3",
        color=ft.colors.WHITE,
        text_align=ft.TextAlign.RIGHT,
        width=field_width,
        border_color=ft.colors.WHITE
    )
    field7 = ft.TextField(
        bgcolor="#000000B3",
        color=ft.colors.WHITE,
        text_align=ft.TextAlign.RIGHT,
        width=field_width,
        border_color=ft.colors.WHITE
    )
    

    background_image_url = "BG3.jpg"

    return ft.Container(
        content=ft.Stack(
            controls=[

                ft.Image(src=background_image_url, fit=ft.ImageFit.COVER),

                ft.Column(
                    controls=[
                        ft.Container(
                            content=ft.Row(
                                [ft.Text("إنشاء ملف", color=ft.colors.WHITE, size=24)],
                                alignment=ft.MainAxisAlignment.CENTER
                            ),
                            margin=ft.margin.only(top=40),
                        ),
                        ft.Container(
                            content=ft.Column(
                                controls=[
                                    ft.Row(
                                        [ft.Text(" إسم الزبون", color=ft.colors.WHITE), field1],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        spacing=8
                                    ),
                                    ft.Row(
                                        [ft.Text(" رقم الهاتف", color=ft.colors.WHITE), field2],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        spacing=8
                                    ),
                                    ft.Row(
                                        [ft.Text(" التاريخ      ", color=ft.colors.WHITE), field3],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        spacing=8
                                    ),
                                    ft.Row(
                                        [ft.Text("نوع السيارة", color=ft.colors.WHITE), field4],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        spacing=8
                                    ),
                                    ft.Row(
                                        [ft.Text("      وصف", color=ft.colors.WHITE), field5],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        spacing=8
                                    ),
                                    ft.Row(
                                        [ft.Text("  تم العمل", color=ft.colors.WHITE), field6],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        spacing=8
                                    ),
                                    ft.Row(
                                        [ft.Text("      السعر", color=ft.colors.WHITE), field7],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        spacing=8
                                    ),
                                    ft.Row(
                                        [
                                            ft.ElevatedButton(
                                                text="إدخال",
                                                bgcolor="#b7e4c7",
                                                color=ft.colors.WHITE,
                                                on_click=on_submit,
                                                elevation=8,  
                                                width=150,  
                                                height=40,  

                                            )

                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                                spacing=16,
                            ),
                            margin=ft.margin.only(top=20),
                            padding=10,
                            border_radius=8,
                            bgcolor="#000000B3",
                            border=ft.Border(
                                left=ft.BorderSide(color="#FFFFFF", width=1),
                                right=ft.BorderSide(color="#FFFFFF", width=1),
                                top=ft.BorderSide(color="#FFFFFF", width=1),
                                bottom=ft.BorderSide(color="#FFFFFF", width=1)
                            ),
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=16,
                ),
            ],
        ),
        bgcolor=ft.colors.TRANSPARENT,
    )
