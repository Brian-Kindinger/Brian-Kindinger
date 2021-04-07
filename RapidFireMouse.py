from pynput.mouse import Listener
from pynput.mouse import Button, Controller
import time 

# Constants
HOLD_DURATION = 0.5  #seconds
RAPIDFIRE_PERIOD = 0.05 #seconds

# Global Variables
gTimeLeftClick = 0.0
gTimeRightClick = 0.0
gPressedLeft = False
gPressedRight = False

# Functions
def on_click(x, y, button, pressed):
    global gTimeLeftClick, gTimeRightClick
    global gPressedLeft, gPressedRight

    if button == Button.left:
        if pressed:
            gTimeLeftClick=time.time()*1000.0
            gPressedLeft = True
        if not pressed:
            gPressedLeft= False
    elif button == Button.right:
        if pressed:
            gTimeRightClick=time.time()*1000.0
            gPressedRight = True
        if not pressed:
            gPressedRight= False

# Main
def main():
    global gTimeLeftClick, gTimeRightClick
    global gPressedLeft, gPressedRight

    print("Main Started")

    mouseCont = Controller()
    print("Mouse Controller Started")

    listener = Listener(on_click=on_click)
    listener.start()

    while True:
        if gPressedLeft:
            print("Left Click duration =" + str(time.time()*1000 - gTimeLeftClick))
            if ((time.time()*1000-gTimeLeftClick) > HOLD_DURATION*1000):
                mouseCont.click(Button.left, 2)

        if gPressedRight:
            print("Right Click duration =" + str(time.time()*1000 - gTimeRightClick))
            if ((time.time()*1000-gTimeRightClick) > HOLD_DURATION*1000):
                mouseCont.click(Button.right, 2)

        time.sleep(RAPIDFIRE_PERIOD)

if __name__ == "__main__":
    main()