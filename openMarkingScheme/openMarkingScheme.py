import pyautogui as pag
import pyperclip
from win32gui import IsWindowVisible, GetWindowText, EnumWindows, ShowWindow, SetForegroundWindow, SystemParametersInfo
from global_hotkeys import *
import win32clipboard
import time
import keyboard

IS_ALIVE = True
pag.PAUSE = 0


DELAY = 0.45


def getCopied():
    # delay is required as a measure to prevent `ctrl + x` mixing with the hotkey entered
    # time.sleep(DELAY)

    win32clipboard.OpenClipboard()
    try:
        # getting current data for resetting clipboard later
        prevClip = win32clipboard.GetClipboardData()
    except TypeError:
        win32clipboard.SetClipboardData(win32clipboard.CF_UNICODETEXT, " ")
    win32clipboard.CloseClipboard()

    # get currently selected text
    pag.hotkey("ctrl", "c")
    time.sleep(0.1)

    # get clipboard data
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()

    # resetting clipboard data to previous content
    try:
        win32clipboard.SetClipboardData(
            win32clipboard.CF_UNICODETEXT, prevClip)
    except:
        print("line 36: prevClip set error")

    win32clipboard.CloseClipboard()

    return data


def bringWindowToFocus(partial_window_name):
    def window_enum_handler(hwnd, resultList):
        if IsWindowVisible(hwnd) and GetWindowText(hwnd) != '':
            resultList.append((hwnd, GetWindowText(hwnd)))
    handles = []
    EnumWindows(window_enum_handler, handles)
    for i in handles:
        if str(partial_window_name).upper() in str(i[1]).upper():
            ShowWindow(i[0], 3)
            SetForegroundWindow(i[0])
            return True
    return False


def ms():
    time.sleep(DELAY)
    bringWindowToFocus(" - Microsoft Edge")
    pag.hotkey("alt", "d")
    # pag.hotkey("ctrl", "c")

    data = getCopied()
    pag.hotkey("ctrl", "t")
    pag.write(data.replace("qp", "ms"))
    pag.press("enter")


def exit_application():
    global IS_ALIVE
    stop_checking_hotkeys()
    IS_ALIVE = False


BINDINGS = [
    [["control", "alt", "shift", "s"], None, ms],
    [["control", "shift", "alt", "9"], None, exit_application],
]

# Register all of our keybindings
register_hotkeys(BINDINGS)

# Finally, start listening for keypresses
start_checking_hotkeys()

while IS_ALIVE:
    time.sleep(0.1)
