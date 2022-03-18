import time
import pyautogui as pag
from helpers import findImageTimeout, findImage
pag.PAUSE = 1
pag.click(findImageTimeout("./images/lan.png"))
pag.click(findImageTimeout("./images/intranet.png"))
pag.click(findImageTimeout("./images/connectHover.png"))


while True:
    t1 = time.time()
    pag.write("password")
    pag.press("enter")

    while True:
        print("Still Exists")
        if findImage("./images/verifying.png") == (-1, -1):
            break

    print(round(time.time() - t1, 3))
