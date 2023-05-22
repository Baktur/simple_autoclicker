import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

key_bind = KeyCode(char=input("Keybind > "))
delay = 1 / int(input("Clicks Per Second > "))

mouse = Controller()

def toggle(key):
    if key == key_bind:
        global run
        run = not run

def auto_clicker():
    while True:
        if run:
            mouse.click(Button.left, 1)
        time.sleep(delay)

run = False
auto_click_thread = threading.Thread(target=auto_clicker)
auto_click_thread.start()

with Listener(on_press=toggle) as listener:
    listener.join()