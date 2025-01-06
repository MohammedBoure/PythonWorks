import pyautogui
import time
import keyboard

while True:
    if keyboard.is_pressed('c') or pyautogui.mouseDown(button='middle'):
        pyautogui.mouseDown(button='left')
        time.sleep(0.2)
        pyautogui.mouseUp(button='left')
        


    time.sleep(0.1)
