import pyautogui
import pyperclip
import time
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

picPosition = pyautogui.locateOnScreen('img1.png')
print(picPosition)

if picPosition is None :
    picPosition = pyautogui.locateOnScreen('img2.png')
    print(picPosition)

if picPosition is None :
    picPosition = pyautogui.locateOnScreen('img3.png')
    print(picPosition)

clickPosition = pyautogui.center(picPosition)
pyautogui.doubleClick(clickPosition)

pyperclip.copy('파이썬 auto kakaotalk test')
pyautogui.hotkey('ctrl','v')
time.sleep(1.0)

pyautogui.write(['enter'])
time.sleep(1.0)

pyautogui.write(['escape'])
time.sleep(1.0)