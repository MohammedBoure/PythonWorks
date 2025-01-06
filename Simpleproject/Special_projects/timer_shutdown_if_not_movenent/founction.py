import pyautogui
import subprocess
from time import sleep


def screnshot_pixel():
    screenshot = pyautogui.screenshot()
    width, height = screenshot.size
    pixel_data = screenshot.load()
    list_data_image = []
    for y in range(height):
        for x in range(width):
            r, g, b = pixel_data[x, y]
            list_data_image.append(((x,y),(r,g,b)))
    return list_data_image

def main(dt):
    sleep(5)
    while True:
        a = screnshot_pixel()
        sleep(dt)
        b = screnshot_pixel()

        if a==b:
            print(True)
            subprocess.run(["shutdown", "/s", "/t", "0"])
        else:
            print(False)