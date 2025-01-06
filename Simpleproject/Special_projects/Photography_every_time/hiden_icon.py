import pystray
from pystray import MenuItem as item
from PIL import Image
from replace_text import read_file,write_file
import win32gui
import win32con
import os


def hiden_app():
    hwnd = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(hwnd, win32con.SW_HIDE)

file_path = "file.txt"
file_content = read_file(file_path)

hiden_app()
icon_closed = False

def main():
    def on_quit_clicked(icon, item):
        icon.stop()
        global icon_closed
        icon_closed = True

    image_path = "diaphragm.png"
    icon_image = Image.open(image_path)
    icon = pystray.Icon("MyApp", icon_image, "MyApp")
    icon.menu = (item('Quit', on_quit_clicked),)
    icon.run()

    if icon_closed and file_content is not None:
        new_content = file_content.replace("", "1")
        write_file(file_path,new_content)
        os.system("exit")        
main()
