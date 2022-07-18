
import pyautogui
import time
from PIL import ImageGrab
from PIL import ImageOps
from numpy import *



restart_btn=(676,267)
dinasour=(423,298)

def restart_game():
    pyautogui.click(restart_btn)

def grab_image():
    pixel_box=(dinasour[0]+55,dinasour[1],dinasour[0]+145, dinasour[1]+5 )
    image=ImageGrab.grab(pixel_box)
    gray_image=ImageOps.grayscale(image)
    image_array=array(gray_image.getcolors())
    return image_array.sum()

def jump():
    time.sleep(0.2)
    pyautogui.keyDown("space")



time.sleep(4)
restart_game()


while True:
    grab_image()
    if (grab_image() != 697):
        jump()         
        time.sleep(0.1)

