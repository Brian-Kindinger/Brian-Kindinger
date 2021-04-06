from pynput.mouse import Listener
from pynput.mouse import Button, Controller
import time 

# Constants
HOLD_TIME = 0.5  #seconds
POLL_TIME = 0.05 #seconds

# Global Variables
gTime = 0.0
gPressed = False

# Functions
def on_click(x, y, button, pressed):
    global gTime
    global gPressed

    if pressed:
        gTime=time.time()*1000.0
        gPressed = True
    if not pressed:
        gPressed = False

# Main
def main():
    global gPressed
    global gTime
    print("Main Started")

    mouseCont = Controller()
    print("Mouse Controller Started")

    listener = Listener(on_click=on_click)
    listener.start()

    while True:
        if gPressed == True:
            print("gTime ="+ str(gTime) +" clicktime =" + str(time.time()*1000 - gTime))
            if ((time.time()*1000-gTime) > HOLD_TIME*1000):
                print(gTime)
                mouseCont.click(Button.left, 2)
        time.sleep(POLL_TIME)

if __name__ == "__main__":
    main()