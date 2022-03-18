import pyautogui as pag
import time
pag.PAUSE = 0
bars = [
    (672, 60, 1, 400),
    (756, 60, 1, 400),
    (844, 60, 1, 400),
    (935, 60, 1, 400),
]
time.sleep(2)

while True:
    values = []
    for bar in bars:
        image = pag.screenshot(region=bar)

        for pixel in list(reversed(range(0, 400))):
            # print(image.getpixel((0, pixel)))
            pix = image.getpixel((0, pixel))
            r = pix[0]
            g = pix[1]
            b = pix[2]
            exR = 1
            exG = 1
            exB = 1
            tolerance = 10

            # if image.getpixel((0, pixel)) == (1, 1, 1):
            # if pag.pixelMatchesColor(bar[0], bar[1] + bar[3], (1, 1, 1), tolerance=10):
            if (abs(r - exR) <= tolerance) and (abs(g - exG) <= tolerance) and (abs(b - exB) <= tolerance):
                # pag.click(bar[0], pixel + 60)
                # print(bar[0], pixel + 60)
                values.append((bar[0], pixel + 60))
                break

    largest = (0, 0)
    for value in values:
        # print(value)
        if value[1] > largest[1]:
            # print(value)
            largest = value

    if largest[0] == bars[0][0]:
        pag.press("d")
    elif largest[0] == bars[1][0]:
        pag.press("f")
    elif largest[0] == bars[2][0]:
        pag.press("j")
    elif largest[0] == bars[3][0]:
        pag.press("k")

    time.sleep(0.05)
    # if largest != (0, 0):
    #     pag.click(largest)

    # break
    # image.show()
    # break
        # print(bar[0], pixel)
        # if pag.pixelMatchesColor(bar[0], pixel, (0, 0, 0)):
        #     print(bar[0], pixel)
        #     # pag.click(bar[0], pixel)
    # if image
