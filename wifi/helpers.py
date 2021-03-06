import cursor
import os
import time
import pyautogui as pag
import json
import yaml
from datetime import datetime
from collections import OrderedDict
from rich.progress import Progress
from win32gui import IsWindowVisible, GetWindowText, EnumWindows, ShowWindow, SetForegroundWindow, SystemParametersInfo
CUR_PATH = os.path.dirname(os.path.realpath(__file__))
cursor.hide()
defaultTimeout = 600


def loadFiles():
    CURR_DAY_NUM = datetime.today().weekday()

    if not os.path.exists(os.path.dirname(f"{CUR_PATH}/config/classes.yaml")):
        try:
            os.makedirs(os.path.dirname(f"{CUR_PATH}/config/classes.yaml"))
        except OSError as exc:  # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise

    # making new classes file if it doesnt already exist
    if not os.path.exists(f"{CUR_PATH}/config/classes.yaml"):
        file = open(f"{CUR_PATH}/config/classes.yaml", "w")
        SAMPLE_CLASS = {
            "Default Class": {
                "code": 'Change code',
                "password": 'Change Password',
                "time_friday": "00:00",
                "time_of_leaving_friday": "00:00",
                "time_of_leaving_weekday": "00:00",
                "time_weekday": "00:00"
            }
        }

        yaml.dump(SAMPLE_CLASS, file)
        file.close()

    if not os.path.exists(f"{CUR_PATH}/config/config.yaml"):
        file = open(f"{CUR_PATH}/config/config.yaml", "w")
        SAMPLE_CONFIG = {
            "delayBetweenActions": 0.6,
            "globalConfidence": 0.99,
            "requireConfirmationBeforeJoining": True,
            "requireConfirmationBeforeLeaving": True
        }

        yaml.dump(SAMPLE_CONFIG, file)
        file.close()

    # importing external files
    with open(f"{CUR_PATH}/config/config.yaml", 'r') as stream:
        try:
            SETUP = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)

    with open(f"{CUR_PATH}/config/classes.yaml", 'r') as stream:
        try:
            CLASS_INFO = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)

    # sorting classes
    # https://stackoverflow.com/questions/42398375/sorting-a-dictionary-of-dictionaries-python
    if CURR_DAY_NUM == 4:
        # friday timings
        CLASS_INFO = OrderedDict(
            sorted(CLASS_INFO.items(), key=lambda x: x[1]["time_friday"]))
    else:
        # any other day
        CLASS_INFO = OrderedDict(
            sorted(CLASS_INFO.items(), key=lambda x: x[1]["time_weekday"]))

    return SETUP, CLASS_INFO


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def findImage(imageUrl: str, confidence: int = 0.9):
    try:
        x, y = pag.locateCenterOnScreen(
            f"{imageUrl}", confidence=confidence)
        return (x, y)
    except TypeError:
        return (-1, -1)


def enterTextInput(x: int, y: int, text: str, message: str):
    pag.click(x=x, y=y)
    pag.write(text.replace(" ", ""))
    pag.press("enter")


def findImageTimeout(imageUrl: str, timeout: int = defaultTimeout, confidence: int = 0.90):
    i = 1
    while True:
        if i <= timeout:
            try:
                x, y = pag.locateCenterOnScreen(f"{imageUrl}", confidence=confidence)
            except TypeError:
                time.sleep(1)
                i += 1
                continue
            break
        else:
            return (-1, -1)

    return (x, y)


def findAndClick(imageUrls: list, message: str, errorMessage: str,  timeout: int = defaultTimeout, confidence: int = 0.95):
    output = {}
    i = 0

    with Progress(transient=True) as progress:
        task = progress.add_task(f"{message}...", start=False, total=timeout)

        while not progress.finished:
            if i <= timeout:
                for imageUrl in imageUrls:
                    t1 = time.time()
                    x, y = findImage(imageUrl, confidence)
                    # calculating time taken to find this image
                    t2 = time.time() - t1
                    if x != -1 and y != -1:
                        pag.click(x, y)
                        progress.stop()
                        return {"error": False, "message": None, "coords": {"x": x, "y": y}}
                        break
                    else:
                        # calculating amount to increase based on time taken by image to attempt to find
                        amountToIncrease = (
                            len(imageUrls) * t2 / len(imageUrls))
                        i += amountToIncrease
                        progress.update(task, advance=amountToIncrease)
            else:
                progress.stop()
                return {"error": True, "message": f"Timed Out: {errorMessage}"}


def findAndInputText(imageUrls: list, message: str, errorMessage: str, textToInput: str, timeout: int = defaultTimeout, confidence: int = 0.95):
    output = {}
    i = 0

    with Progress(transient=True) as progress:
        task = progress.add_task(f"{message}...", start=False, total=timeout)

        while not progress.finished:
            if i <= timeout:
                for imageUrl in imageUrls:
                    t1 = time.time()
                    x, y = findImage(imageUrl, confidence)
                    # calculating time taken to find this image
                    t2 = time.time() - t1
                    if x != -1 and y != -1:
                        pag.click(x, y + 60)
                        pag.write(textToInput.replace(" ", ""))
                        pag.press("enter")
                        progress.stop()
                        return {"error": False, "message": None}
                    else:
                        # calculating amount to increase based on time taken by image to attempt to find
                        amountToIncrease = (
                            len(imageUrls) * t2 / len(imageUrls))
                        i += amountToIncrease
                        progress.update(task, advance=amountToIncrease)
            else:
                progress.stop()
                return {"error": True, "message": f"Timed Out: {errorMessage}"}
