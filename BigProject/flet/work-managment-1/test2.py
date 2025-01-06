import flet as ft

def main(page: ft.Page):
    page.title = "screen for scroll"
    
    items = [ft.Text(f"Item {i}", size=20) for i in range(50)]

    scroll_view = ft.(content=ft.Column(items, spacing=10))

    page.add(scroll_view)
ft.app(target=main)
