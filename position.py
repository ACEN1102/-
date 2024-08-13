import time

import pyautogui


def get_position():
    position = pyautogui.position()
    print(position)


while True:
    get_position()
    time.sleep(5)
