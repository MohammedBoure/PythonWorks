import pyautogui
import time
import keyboard

pressed = True

while True:
    if keyboard.is_pressed('i'):
        pressed = not pressed
        if pressed:
            pyautogui.mouseUp(button='right')
        if not pressed:
            pyautogui.mouseDown(button='right')

    time.sleep(0.1)

