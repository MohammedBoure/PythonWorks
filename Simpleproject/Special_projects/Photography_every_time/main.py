import cv2
import os
from time import sleep
from datetime import datetime
import hiden_app
from replace_text import read_file,write_file



file_path_text = "file.txt"

file_content = read_file(file_path_text)
if file_content is not None:
    new_content = file_content.replace("1", "")
    write_file(file_path_text, new_content)


input_timer_cup = 900         #seconde
def split_time_date(x):
    list_x = x.split("/")
    date_time = list_x[0]+"-"+list_x[1]+"-"+list_x[2]
    #list_x = date_time.split(":")
    #date_time = list_x[0]+"-"+list_x[1]+"-"+list_x[2]
    return date_time

hiden_app.hiden_app()
x = 0
while True:
    x += 1
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        continue

    print(read_file(file_path_text))
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y")

    ret, frame = cap.read()
    if ret:
        cv2.imwrite("images/"+str(x)+"_"+split_time_date(dt_string)+".jpg", frame)
    try:
        file_path = os.path.join("",split_time_date(str(x)+"_"+str(int(dt_string[0]+dt_string[1])-1)+now.strftime("/%m/%Y"))+".jpg")
    except:
        pass
    if os.path.exists(file_path):
        os.remove(file_path)


    try:
        if read_file(file_path_text)[0] == "1":
            os.system("exit")
            print("zzzz")
            cap.release()

            break
    except:
        pass
    cap.release()
    sleep(input_timer_cup)

cv2.destroyAllWindows()

