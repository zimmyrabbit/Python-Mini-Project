#pip install pyautogui
# 마우스와 키보드를 자동제어하기 위한 라이브러리

#pip install pyperclip
# 클립보드에서 값을 복사 하거나 붙여넣기 용도로 사용

import pyautogui
import time

while True:
    print(pyautogui.position())
    time.sleep(0.1)