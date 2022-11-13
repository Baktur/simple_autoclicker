import time
import threading
from pynput.mouse import Button,Controller
from pynput.keyboard import Listener,KeyCode

keyBind=KeyCode(char=input("Keybind > "))
delay=(1/(float(input("Clicks Per Second > "))))

mouse=Controller()
def toggle(key):
    if key==keyBind:
        global run
        run=not run
def autoClicker():
    while True:
        if run:
            mouse.click(Button.left,1)
        time.sleep(delay)

run=False
autoClickThread=threading.Thread(target=autoClicker)
autoClickThread.start()
with Listener(on_press=toggle) as listener:
    listener.join()