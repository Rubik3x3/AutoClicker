from random import random
from threading import Thread
from time import sleep
from pynput.mouse import Controller,Button
from pynput.keyboard import KeyCode, Listener

delay = 0.1
mouse = Controller()

class AutoClicker(Thread):
    clicking = False
    def run(self):
        while True:
            if AutoClicker.clicking:
                mouse.click(Button.left)
            sleep(delay * random() + 1/2 * delay)

def keypress(key):
    if key == KeyCode(char="{"):
        AutoClicker.clicking = not AutoClicker.clicking

AutoClicker().start()

with Listener(on_press=keypress) as listener:
    listener.join()