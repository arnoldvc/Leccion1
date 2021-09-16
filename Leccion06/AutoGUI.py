import pyautogui
import time
import pyperclip

pyautogui.PAUSE = 1
# Paso 1

# pyautogui.hotkey('CTRL','Esc')
pyautogui.press('win')
pyautogui.write('Firefox')
pyautogui.press('enter')
link = 'https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga'
# pyautogui.write('https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga')
pyperclip.copy(link)
pyautogui.hotkey('ctrl','v')
pyautogui.press('enter')

# Paso 2
time.sleep(5)
pyautogui.click(401, 276, clicks=2)




