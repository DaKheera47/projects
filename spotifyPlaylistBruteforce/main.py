import pyautogui as pag
import time
import keyboard

pag.PAUSE = 0.3
coords = pag.locateOnScreen("bar.png", confidence=0.8, grayscale=True)
BAR_PERCENTAGE = 0.35

def read():
    keyboard.read_key()


def like():
    try:
        coords = pag.locateOnScreen("like.png")
        coords = pag.center(coords)
        print(coords)
        pag.click(coords)
    except:
        pass


def nextSong():
    pag.press("nexttrack")
    pag.click(coords.left + (coords.width * BAR_PERCENTAGE),
              coords.top + (coords.height * 0.50))


def previous():
    pag.press("prevtrack")
    pag.press("prevtrack")
    pag.click(coords.left + (coords.width * BAR_PERCENTAGE),
              coords.top + (coords.height * 0.50))


def my_exit():
    pass


keyboard.add_hotkey("n", nextSong)
keyboard.add_hotkey("p", previous)
keyboard.add_hotkey("l", like)
keyboard.add_hotkey("esc", my_exit)

while True:
    read()
