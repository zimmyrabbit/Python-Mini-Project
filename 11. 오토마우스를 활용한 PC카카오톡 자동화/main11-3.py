import pyautogui
import pyperclip
import time
import threading
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def send_message() :
    threading.Timer(10, send_message).start()

    picPosition = pyautogui.locateOnScreen('img1.png')

    if picPosition is None :
        picPosition = pyautogui.locateOnScreen('img2.png')

    if picPosition is None :
        picPosition = pyautogui.locateOnScreen('img3.png')

    clickPosition = pyautogui.center(picPosition)
    pyautogui.doubleClick(clickPosition)

    pyperclip.copy('파이썬 auto kakaotalk test')
    pyautogui.hotkey('ctrl','v')
    time.sleep(1.0)
    
    pyautogui.write(['enter'])
    time.sleep(1.0)

    pyautogui.write(['escape'])
    time.sleep(1.0)

send_message()