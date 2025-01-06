from PIL import ImageGrab
import os
from time import sleep
import test6
from replace_text import read_file,write_file


def take_screenshot(filename):
    screenshot = ImageGrab.grab()
    screenshot.save(filename)


file_path_text = "file.txt"
file_path_text2 = "num.txt"

file_content = read_file(file_path_text)
file_content2 = read_file(file_path_text)

if file_content is not None:
    new_content = file_content.replace("1", "")
    write_file(file_path_text, new_content)


input_timer_cup = 6          #seconde


test6.hiden_app()


if read_file(file_path_text2)=="":
    new_content = file_content2.replace("", "0")
    write_file(file_path_text2, new_content)

x = read_file(file_path_text2)

while True:
    x = int(x) + 1

    if __name__ == "__main__":
        filename = str(x) + ".png"
        take_screenshot("name/"+filename)

    try:
        if read_file(file_path_text)[0] == "1":
            os.system("exit")
            break
    except:
        pass

    new_content2 = file_content2.replace("", str(x))
    write_file(file_path_text2, new_content2)

    sleep(input_timer_cup)


