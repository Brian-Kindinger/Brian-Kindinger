from pynput.mouse import Listener
from pynput.mouse import Button, Controller
import time 

mouse = Controller()
gTime = 0.0
gPressed = False

def on_click(x, y, button, pressed):
    global gTime
    global gPressed
    print('{0} at {1}'.format(
        'Pressed' if pressed else 'Released',
        (x, y)))
    if pressed:
        gTime=time.time()*1000.0
        gPressed = True
    if not pressed:
        gPressed = False


with Listener(on_click=on_click) as listener:
    listener.join()

def main():
    print("Hello World!")
    if gPressed == True:
        if ((gTime - time.time()*1000) > 1000):
            print(gTime)
            mouse.click(Button.left, 2)
    time.sleep(0.1)

if __name__ == "__main__":
    main()