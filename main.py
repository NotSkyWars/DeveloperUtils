from dataclasses import dataclass
from win32gui import GetWindowText, GetForegroundWindow
import win32api as win32api
import win32con as win32con
import time
import keyboard


def main():
    x = 0
    time.sleep(2)
    isOn = False
    while True:
        _names = GetWindowText(GetForegroundWindow())
        keyboard
        if keyboard.is_pressed('c'):
            isOn = True

        if 'Minecraft' in _names:
            if isOn:
                if keyboard.is_pressed('o'):
                    isOn = False
                win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)
                win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)

                time.sleep(0.04)


if __name__ == '__main__':
    main()
