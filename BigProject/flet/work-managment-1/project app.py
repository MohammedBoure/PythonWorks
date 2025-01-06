import flet as ft
from home_page import home_page
from search_page import search_page

def main(page: ft.Page):
    page.title = "Multi-Page App"
    page.bgcolor = ft.colors.BLACK
    page.padding = 10
    page.scroll = "auto"


    page.window.width = 375
    page.window.height = 667


    def show_page(page_name):
        page.controls.clear()


        content = ft.Container(
            content=page_content(page_name, page),
            bgcolor=ft.colors.TRANSPARENT,
            padding=10,
        )

        footer = ft.Container(
            content=ft.Row(
                controls=[
                    ft.IconButton(
                        ft.icons.HOME,
                        on_click=lambda e: show_page("home"),
                        icon_color=ft.colors.WHITE,
                    ),
                    ft.IconButton(
                        ft.icons.SEARCH,
                        on_click=lambda e: show_page("search"),
                        icon_color=ft.colors.WHITE,
                    ),
                    ft.IconButton(
                        ft.icons.HISTORY,
                        on_click=lambda e: show_page("recent"),
                        icon_color=ft.colors.WHITE,
                    ),
                    ft.IconButton(
                        ft.icons.EDIT,
                        on_click=lambda e: show_page("edit"),
                        icon_color=ft.colors.WHITE,
                    ),
                    ft.IconButton(
                        ft.icons.SETTINGS,
                        on_click=lambda e: show_page("settings"),
                        icon_color=ft.colors.WHITE,
                    ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_AROUND,
            ),
            bgcolor=ft.colors.GREY_800,
            padding=5,
            border_radius=ft.border_radius.all(5),
            width="100%",
            height=50,
        )

        page.add(
            ft.Stack(
                controls=[
                    ft.Container(
                        width=page.window.width,
                        height=page.window.height,
                        bgcolor=ft.colors.TRANSPARENT,
                    ),
                    content,
                    footer,
                ]
            )
        )
        page.update()

    def page_content(page_name, page):
        if page_name == "home":
            return home_page()
        elif page_name == "search":
            return search_page(page)
        elif page_name == "recent":
            return recent_page()
        elif page_name == "edit":
            return edit_page()
        elif page_name == "settings":
            return settings_page()
        return ft.Container()

    def recent_page():
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text("Recent Page", color=ft.colors.WHITE),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=10,
            ),
            bgcolor="#212323",
            padding=10,
        )

    def edit_page():
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text("Edit Page", color=ft.colors.WHITE),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=10,
            ),
            bgcolor="#212323",
            padding=10,
        )

    def settings_page():
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text("Settings Page", color=ft.colors.WHITE),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=10,
            ),
            bgcolor=ft.colors.WHITE_OPACITY40,
            padding=10,
        )

    show_page("home")

ft.app(target=main)
