import pyautogui as pag
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
for loc in pag.locateAllOnScreen("icon.png"):
    loc = pag.center(loc)
    pag.click(loc)

    # locate class teacher comments
    x, y = findImageTimeout("classTeacherComments.png")
    pag.click(x, y + 20)

    # select all text and copy
    pag.hotkey("ctrl", "a")
    pag.hotkey("ctrl", "c")

    # print clipboard
    comments = pyperclip.paste()
    print(comments)

    # locate achievements
    x, y = findImageTimeout("achievements.png")
    pag.click(x, y + 20)

    # select all text and copy
    pag.hotkey("ctrl", "a")
    pag.hotkey("ctrl", "c")

    # print clipboard
    achievements = pyperclip.paste()
    print(achievements)

    # alt f4
    pag.hotkey("alt", "f4")

    pag.moveTo(loc.x + 962, loc.y)
    pag.click()

    # locate class teacher comments
    x, y = findImageTimeout("classTeacherComments.png")
    pag.click(x, y + 20)
    pag.typewrite(comments)

    # locate achievements
    x, y = findImageTimeout("achievements.png")
    pag.click(x, y + 20)
    pag.typewrite(achievements)

    # alt f4
    pag.hotkey("alt", "f4")
