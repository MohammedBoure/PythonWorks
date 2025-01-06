import pyautogui

size = pyautogui.size()
position = pyautogui.position()

gravity = int(input("g = "))*100
print("to exit drag the mouse to a corner")
pyautogui.PAUSE = 1/gravity
while True:
    for x in range(gravity):
        pyautogui.move(0, 1)