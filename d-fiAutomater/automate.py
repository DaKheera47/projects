import os
import pyautogui as pag
import time
import yaml
import json

def findImage(imageUrl, message, confidence):
    i = 1

    while True:
        time.sleep(1)
        try:
            x, y = pag.locateCenterOnScreen(
                imageUrl, confidence=confidence, grayscale=True)
        except TypeError:
            print(f"{message} (attempts: {i})", end="\r")
            i += 1
            continue
        break

    return (x, y)

time.sleep(5)
i = 18
while i < 49:
    print(f"npm run {i}")
    pag.write(f"npm run {i}")
    pag.press("enter")

    # find out when the song finishes downloading
    searchX, searchY = findImage("arrow.png", "Finding Saved Text", 0.9)
    
    pag.hotkey("ctrl", "c")
    
    pag.write("cls")
    pag.press("enter")
    
    i += 1

