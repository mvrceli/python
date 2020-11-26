import pyautogui
import time
import keyboard
import random
import win32api, win32con


def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.02) 
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

#SCREEN: 102, 135, 1340, 690
#SCOUT A:1237, 455 RGB:(255, 166,   0))
#SCOUT B:1238, 616 RGB: (255, 166,   0))


time.sleep(2)
while keyboard.is_pressed('q') == False:

    #OPEN SCOUT MENU
    click(964, 326)
    time.sleep(1)
    click(1148, 493)
    time.sleep(1)
    wait = True
    wait1 = True
    while wait is True:
        if pyautogui.pixel(1237, 455)[0] == 255:
            click(1237, 455)
            wait = False
        elif pyautogui.pixel(1238, 616)[0] == 255:
            click(1237, 616)
            wait = False
        else:
            time.sleep(10)
            wait = True
    time.sleep(2)
    click(995,676)
    time.sleep(1)
    while wait1 is True:
        if pyautogui.pixel(1242, 220)[0] == 255:
            click(1242, 220)
            wait1 = False
        elif pyautogui.pixel(1242, 379)[0] == 255:
            click(1242, 379)
            wait1 = False
        else:
            time.sleep(10)
            wait1 = True
    time.sleep(1)
    click(82,846)
    time.sleep(2)


    pic = pyautogui.screenshot(region=(180, 158, 1201, 596))
    width, height = pic.size
    time.sleep(4)
    for x in range(0,width,5):
        for y in range(0,height,5):

            r,g,b = pic.getpixel((x,y))

            if b == 16:
                click(x+102, y+135)
                break
    time.sleep(5)
    pic = pyautogui.screenshot(region=(1130, 70, 240, 377))
    width, height = pic.size

    for x in range(0,width,5):
        for y in range(0,height,5):

            r,g,b = pic.getpixel((x,y))

            if b == 16:
                click(x+1124, y+70)
                break
    
    click(82,846)






