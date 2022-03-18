
# Created: 22 Oct 2021
import keyboard
import pyautogui as pag
import time
from inpageTyper import *
# time.sleep(2)

pag.PAUSE = 1
while True:
    input("")
    pag.hotkey("alt", "tab")
    for i in range(7, 16):
        pag.press('end')

        PressKey(54)
        pag.press('left', presses=5)
        ReleaseKey(54)


        PressKey(convertToCode("CTRL"))
        PressKey(convertToCode("v"))
        ReleaseKey(convertToCode("v"))
        ReleaseKey(convertToCode("CTRL"))
        # time.sleep(2)
        # input("")

        # pag.hotkey("ctrl", "v")

        # keyboard.press_and_release('ctrl + v')
        pag.press('up', presses=2)

        pag.press('home')
        pag.press('delete')
        if len(str(i)) >= 2 and i != 11:
            pag.press('delete')

        pag.write(str(i))
        pag.press('down', presses=3)
