import pyautogui, sys
import time as time
print('Press Ctrl-C to quit.')
try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
        pyautogui.moveTo(900, 250)
        pyautogui.click(button='right')
        time.sleep(0.5)
        pyautogui.moveTo(998, 460)
        time.sleep(0.6)
        pyautogui.moveTo(1199, 708)
        time.sleep(0.6)
        pyautogui.click()
        time.sleep(0.6)
        pyautogui.press('enter')
        time.sleep(0.6)
        pyautogui.moveTo(954, 223)
        time.sleep(0.3)
        pyautogui.click()
        time.sleep(0.1)
        pyautogui.click()
        time.sleep(0.8)
        pyautogui.typewrite('Elsker dig!!', interval=0.1)
        time.sleep(0.3)
        pyautogui.moveTo(1753, 167)
        time.sleep(0.8)
        pyautogui.click()
        time.sleep(0.3)
        pyautogui.moveTo(1006, 561)
        time.sleep(0.6)
        pyautogui.click()
        time.sleep(0.3)
        pyautogui.moveTo(948, 230)
        time.sleep(0.6)
        pyautogui.click(button='right')
        time.sleep(0.6)
        pyautogui.moveTo(1016, 646)
        time.sleep(0.6)
        pyautogui.click()
        time.sleep(0.3)
        pyautogui.moveTo(116, 30)
        time.sleep(0.3)
        pyautogui.click(button='right')
        time.sleep(0.3)
        pyautogui.moveTo(150, 66)
        time.sleep(0.6)
        pyautogui.click()
        time.sleep(0.3)
        pyautogui.moveTo(1063, 564)
        time.sleep(0.3)
        pyautogui.click()
        break
except KeyboardInterrupt:
    print('\n')
