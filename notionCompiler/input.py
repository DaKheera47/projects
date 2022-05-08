import pyautogui as pag
import time
pag.PAUSE = 1
data = [
    {
        "name": "9709_s16_qp_61",
        "obtained": "32"
    },
    {
        "name": "9709_w16_qp_61",
        "obtained": "34"
    },
    {
        "name": "9709_s17_qp_61",
        "obtained": "31"
    },
    {
        "name": "9709_w17_qp_61",
        "obtained": "41"
    },
]


for info in data:
    # get variables
    name = info["name"]
    obtained = info["obtained"]

    point = pag.locateCenterOnScreen("new.png")
    pag.click(point)

    pag.typewrite(name, interval=0.1)
    pag.click(pag.locateCenterOnScreen("obtEmpty.png"))
    pag.typewrite(obtained, interval=0.1)
    pag.press("enter")
    pag.click(point)

    time.sleep(60)
