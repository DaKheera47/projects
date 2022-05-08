import pyautogui as pag
import time
import keyboard

pag.PAUSE = 0.3


def read():
    keyboard.read_key()


def skipSong(PERCENTAGE=0.25, sleep=2):
    # time.sleep(sleep)
    bar = pag.locateOnScreen("bar.png", confidence=0.5, grayscale=True)
    coords = pag.center(pag.locateOnScreen(
        "pause.png", confidence=0.8, grayscale=True))

    # get point 30 pixels below coords y
    halfPoint = (coords[0], coords[1] + 30)

    pag.click(halfPoint[0] - (bar.width * (0.5 - PERCENTAGE)), halfPoint[1])


def like():
    try:
        coords = pag.locateOnScreen("like.png")
        coords = pag.center(coords)
        print(coords)
        pag.click(coords)
    except:
        pass


def nextSong(PERCENTAGE=0.25):
    pag.press("nexttrack")
    skipSong(PERCENTAGE=0.25)


def previous(PERCENTAGE=0.25):
    pag.press("prevtrack")
    pag.press("prevtrack")
    skipSong(PERCENTAGE=0.25)


def my_exit():
    pass


keyboard.add_hotkey("n", nextSong)
keyboard.add_hotkey("p", previous)

keyboard.add_hotkey("1", skipSong, args=([0.25]))
keyboard.add_hotkey("2", skipSong, args=([0.5]))
keyboard.add_hotkey("3", skipSong, args=([0.75]))

keyboard.add_hotkey("l", like)
keyboard.add_hotkey("esc", my_exit)

while True:
    read()
