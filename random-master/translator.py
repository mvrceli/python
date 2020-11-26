import pyautogui
from googletrans import Translator
import keyboard
import pyperclip
import subprocess
import time
from pynput.keyboard import Key, Controller

keyboard_type = Controller()

translator = Translator()

while keyboard.is_pressed('esc') == False:
    if keyboard.is_pressed('f2') == True:
        clipboard = ""
        finished = ""
        pyautogui.hotkey('ctrl', 'c')

        # test1 = pyperclip.paste()
        
        clipboard = subprocess.check_output("powershell.exe Get-Clipboard", stderr=subprocess.STDOUT, shell=True)
        clipboard = clipboard.decode() 
        time.sleep(5)
        finished = translator.translate(clipboard)
        translated = finished.text
        print(translated)
        keyboard_type.type(translated)
