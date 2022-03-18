import os
import pyautogui as pag
defaultTimeout = 600


def phraseInString(phrase, string):
    if phrase in string.lower().replace(" ", "").replace("\n", ""):
        return True
    else:
        return False


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def findImageTimeout(imageUrl: str, confidence: int = 0.90):
    while True:
        try:
            x, y = pag.locateCenterOnScreen(f"{imageUrl}", confidence=confidence, grayscale=True)
        except TypeError:
            continue
        break
    return (x, y)
