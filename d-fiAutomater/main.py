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


songLinks = [
    "https://open.spotify.com/track/3f5Wxob4B3xRs55PJET2Vh",
    "https://open.spotify.com/track/6ZW5TjguRHBHr0NOQTzSWr",
    "https://open.spotify.com/track/1iIbaoknvpiWpm70xxZShD",
    "https://open.spotify.com/track/2xw4LfXN78u1AdQZ1co173"
]

file = open("songs.txt", "r").read()

songLinks = file.split("\n")


packageJson = {
    "name": "d-fiautomater",
    "version": "1.0.0",
    "description": "",
    "main": "index.js",
    "scripts": {
        "test": "echo \"Error: no test specified\" && exit 1"
    },
    "author": "",
    "license": "ISC",
    "dependencies": {
        "d-fi": "^2.0.4"
    }
}

i = 0
while i < len(songLinks):

    packageJson["scripts"][f"{i}"] = f"d-fi --url {songLinks[i]} --quality flac"

    i += 1

print(yaml.dump(packageJson, allow_unicode=True, default_flow_style=False))

with open("vibe.json", "w") as f:
    json.dump(packageJson, f)
