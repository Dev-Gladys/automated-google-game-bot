
import pyautogui
import time
from PIL import ImageGrab
from PIL import ImageOps
from numpy import *


"""use a mouse locator to get the coordinate(e.g www.efigureout.com), that gets the x and y codinates of the restart button and the middle
region of the dinosaur when it crashed into the hurdle. Alternatively you can use the pyautogui.position() to get the coordinates"""

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

        
   #NOTES    
 """ def grab_image(): Here your create an imaginary box that is in front of the dinosaur that captures only the white part
of the screen and then grab(screenshot), change to gray and then check  the array of white and gray colors and sum them.
 In the while loop you are saying if the grabbed image is not the sum of what was calculated the dinosaur should jump. 
 If you print the image_array sum,noticed that when the dinosaur is too close to the black hurdle 
 the amount of white and grey changes"""
