from PIL import ImageGrab
import os
from time import sleep



def take_screenshot(filename):
    screenshot = ImageGrab.grab()
    screenshot.save(filename)
    
x = 0
while True:
    sleep(1)
    x = int(x) + 1
    filename = str(x) + ".png"
    take_screenshot("D:/"+filename)



