from random import randrange
import pyautogui

pyautogui.FAILSAFE = False

screenSize = pyautogui.size()
height = screenSize[0]
width = screenSize[1]

while True:
    y = randrange(height)
    x = randrange(width)
    pyautogui.moveTo(x, y, 2)
    pyautogui.press('shift')
