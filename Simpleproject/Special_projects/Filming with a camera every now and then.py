import cv2
import os
from time import sleep
from datetime import datetime
import win32gui
import win32con


def hiden_app():
    hwnd = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(hwnd, win32con.SW_HIDE)


input_timer_cup = 1800           #seconde

def split_time_date(x):
    list_x = x.split("/")
    date_time = list_x[0]+"-"+list_x[1]+"-"+list_x[2]
    #list_x = date_time.split(":")
    #date_time = list_x[0]+"-"+list_x[1]+"-"+list_x[2]
    return date_time

x = 0
#hiden_app()
while True:
    x += 1
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        continue

    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y")

    ret, frame = cap.read()
    if ret:
        cv2.imwrite(str(x)+"_"+split_time_date(dt_string)+".jpg", frame)
    try:
        file_path = os.path.join("",split_time_date(str(x)+"_"+str(int(dt_string[0]+dt_string[1])-1)+now.strftime("/%m/%Y"))+".jpg")
    except:
        pass
    if os.path.exists(file_path):
        print(True)
        os.remove(file_path)
    else:
        print(False)
    cap.release()
    sleep(input_timer_cup)

cv2.destroyAllWindows()
