import time
import keyboard

press_duration = 0.01
val = True

def simulate_esc_press(duration):
    keyboard.press('esc')
    time.sleep(duration)
    keyboard.release('esc')


#  +° and =) and =- and +_
while True:       
    if keyboard.is_pressed(')') and keyboard.is_pressed('='):
        simulate_esc_press(press_duration)
        keyboard.release(')')
        keyboard.release('=')

