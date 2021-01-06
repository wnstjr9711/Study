import pyautogui
import time

myposition = pyautogui.position()
check = 1181, 208
print(myposition)
# check =
while 1:
    time.sleep(0.5)
    pyautogui.moveTo(myposition)
    pyautogui.click()
    pyautogui.moveTo(1181, 208)
    pyautogui.click()
