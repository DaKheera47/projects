import pyautogui as pag
import win32clipboard
import time

# At 67% zoom on edge.

pag.hotkey("alt", "tab")

stars = []

pag.PAUSE = 0.5

file = open("out.txt","a") 

for star in pag.locateAllOnScreen("star.png"):
    stars.append(star)

for star in stars:
    # move to center of tree dots
    s = pag.center(star)
    pag.moveTo(x=s.x + 741, y=s.y, duration=3)
    time.sleep(2)
    pag.click()
    
    # click on share
    pag.moveRel(xOffset=0, yOffset=52, duration=1)
    pag.click()

    # click on generate link
    time.sleep(5)
    pag.moveTo(x=833, y=345, duration=1)
    pag.click()
    # click on copy generated link
    time.sleep(5)
    pag.moveTo(x=833, y=345, duration=1)
    pag.click()

    # get clipboard data
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()

    # write to txt file
    file.write(f"{data}\n")
    print(f"wrote: {data}")