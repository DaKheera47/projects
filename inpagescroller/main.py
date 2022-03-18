from pynput.mouse import Listener
from pynput.keyboard import Key, Controller
import win32gui

w = win32gui
keyboard = Controller()

def on_scroll(x, y, dx, dy):
    if "InPage" in w.GetWindowText(w.GetForegroundWindow()):

        if dy == -1:
            # send shift + pagedown
            with keyboard.pressed(Key.shift):
                keyboard.press(Key.page_down)
                keyboard.release(Key.page_down)
                keyboard.press(Key.page_down)
                keyboard.release(Key.page_down)

        if dy == 1:
            # send shift + pageup
            with keyboard.pressed(Key.shift):
                keyboard.press(Key.page_up)
                keyboard.release(Key.page_up)
                keyboard.press(Key.page_up)
                keyboard.release(Key.page_up)

# Collect events until released
with Listener(on_scroll=on_scroll) as listener:
    listener.join()