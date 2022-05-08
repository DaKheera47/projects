import pyautogui as pag
from pyautogui import Point
import time
import pyperclip


def findImageTimeout(imageUrl: str, timeout: int = 10, confidence: int = 0.90):
    i = 1
    while True:
        if i <= timeout:
            try:
                x, y = pag.locateCenterOnScreen(
                    f"./{imageUrl}", confidence=confidence)
            except TypeError:
                time.sleep(1)
                i += 1
                continue
            break
        else:
            return (-1, -1)

    return (x, y)


pag.PAUSE = 0.5

# locate all on screen
for loc in pag.locateAllOnScreen("tick.png", confidence=0.9):
    loc = pag.center(loc)
    pag.click(loc.x - 140, loc.y)

    time.sleep(1)
    pag.click(Point(x=451, y=275))
    # pag.moveRel(240, 50)
    pag.click()

    # select all text and copy
    pag.hotkey("ctrl", "a")
    pag.hotkey("ctrl", "c")

    # print clipboard
    assessment = pyperclip.paste()
    print(assessment)

    # in new window
    pag.click(loc.x + 730, loc.y)

    time.sleep(1)
    # text box
    pag.click(Point(x=451 + 960, y=275))

    pag.hotkey("ctrl", "a")
    pag.hotkey("ctrl", "v")

    pag.click(findImageTimeout("save.png"))
    pag.click(findImageTimeout("ok.png", confidence=0.8))
    print("\n" * 2)
