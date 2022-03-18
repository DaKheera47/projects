from win32gui import IsWindowVisible, GetWindowText, EnumWindows, ShowWindow, SetForegroundWindow, SystemParametersInfo
import pyautogui as pag


def bringWindowToFocus(partial_window_name):
    def window_enum_handler(hwnd, resultList):
        if IsWindowVisible(hwnd) and GetWindowText(hwnd) != '':
            resultList.append((hwnd, GetWindowText(hwnd)))
    handles = []
    EnumWindows(window_enum_handler, handles)
    for i in handles:
        if str(partial_window_name).upper() in str(i[1]).upper():
            print(str(i[1]).upper())
            ShowWindow(i[0], 3)
            SetForegroundWindow(i[0])
            return True
    return False


bringWindowToFocus("meet -")
pag.hotkey("ctrl", "d")
# bringWindowToFocus("thi-ihtr-tuv")
