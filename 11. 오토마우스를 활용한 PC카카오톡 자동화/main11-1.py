import pyautogui
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