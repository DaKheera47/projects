import pyautogui as pag
import time

pag.PAUSE = 1


for j in range(0, 1):
    # pag.click(x=390, y=568)
    for i in range(0, 5):
        # item
        pag.click(x=390 + (i * 125), y=559)

    # # plus
    # pag.click(x=1021, y=549, clicks=5)

    # # ok
    # pag.click(x=864, y=597)

    # accept
    pag.click(x=782, y=395)

    # continue
    pag.click(x=865, y=609)

    time.sleep(2)

    # accept new thing
    pag.click(x=1082, y=757)

# time.sleep(2)

# # scroll down
# pag.press("down", presses=10, interval=0.1)
