import time

import mouse
import keyboard
import os


def main():
    isOn = False
    oriX = 1280
    oriY = 720
    while True:
        if keyboard.is_pressed('p'):
            isOn = True
            mouse.move(oriX, oriY)
        if isOn:
            if keyboard.is_pressed('o'):
                isOn = False
            y = 0
            x = 0
            posx = mouse.get_position().__str__().replace("(", "").replace(")", "").split(",")[0]
            posy = mouse.get_position().__str__().replace("(", "").replace(")", "").split(",")[1]
        if oriY > int(posy):
            y = 40
        else:
            y = -20
        if (oriX > int(posx)):
            x = 40
        else:
            x = -20
        mouse.move(int(posx) + x, int(posy) + y)
        mouse.right_click()
        print(posx)
        print(posy)
        time.sleep(2)


if __name__ == '__main__':
    main()
