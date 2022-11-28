import pyautogui
import time
import pyperclip

weather = ['서울 날씨','인천 날씨','대전 날씨','부산 날씨','광주 날씨']

#addr_x = 642
#addr_y = 298
addr_x = 300
addr_y = 64
start_x = 249
start_y=304
end_x = 1085
end_y = 814

for regionWeather in weather:
    pyautogui.moveTo(addr_x, addr_y,1)
    time.sleep(0.2)
    pyautogui.click()
    time.sleep(0.2)
    pyautogui.typewrite('www.naver.com', interval=0.1)
    pyautogui.write(['enter'])
    time.sleep(1)

    pyperclip.copy(regionWeather)
    pyautogui.hotkey('ctrl','v')
    time.sleep(0.5)
    pyautogui.write(['enter'])
    time.sleep(1)

    save_path = '10.오토마우스를 활용한 웹페이지 자동화\\' + regionWeather + '.png'
    pyautogui.screenshot(save_path, region=(start_x, start_y, end_x-start_x, end_y-start_y))