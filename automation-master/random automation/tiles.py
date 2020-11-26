import pyautogui
import time
import keyboard
import random
import win32api, win32con

# #Tile 1 Position: X:  585 Y:  625 RGB: ( 77,  80, 115)
# #Tile 2 Position: X:  682 Y:  640 RGB: (  0,   0,   0)
# #Tile 3 Position: X:  770 Y:  655 RGB: ( 79,  82, 116)
# #Tile 4 Position: X:  869 Y:  650 RGB: ( 80,  83, 116)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.02) #This pauses the script for 0.01 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)


while keyboard.is_pressed('q') == False:
    
    if pyautogui.pixel(580, 580)[0] == 0:
        click(581, 580)
    if pyautogui.pixel(682, 640)[0] == 0:
        click(682, 580)
    if pyautogui.pixel(770, 655)[0] == 0:
        click(770, 575)
    if pyautogui.pixel(869, 650)[0] == 0:
        click(869, 570)