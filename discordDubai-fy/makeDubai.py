import pyautogui as pag
from pyautogui import Point
from helpers import findImageTimeout, phraseInString, clear
import pyperclip
import time

pag.PAUSE = 0.5
notFound = True

while notFound:
    allVcs = [pag.center(e) for e in list(pag.locateAllOnScreen('vc.PNG', confidence=0.9))]

    for vc in allVcs:
        pag.click(vc)

        pag.click(findImageTimeout("voiceConnected.png"))
        pag.moveTo(Point(x=117, y=675))
        pag.dragRel(210, duration=0.2)
        pag.hotkey("ctrl", "c")

        if phraseInString("dubai", pyperclip.paste()):
            pag.click(findImageTimeout("voiceConnected.png"))
            notFound = False
            break
        else:
            pag.click(findImageTimeout("disconnect.png"))
