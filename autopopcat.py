import pyautogui
import threading
import time
from pynput.keyboard import Key, Controller

pyautogui.FAILSAFE = True

keyboard = Controller()
thd_quit = 0

for i in range(3):
    print(i)
    time.sleep(1)

def press_a():
    while thd_quit == 0:
        keyboard.press('a')
        keyboard.release('a')
        time.sleep(0.001)
    exit()

def failsafe():
    global thd_quit
    try:
        while 1:
            pyautogui.press('c')
    except:
        print("Quit")
        thd_quit = 1
        exit()


a_thread = threading.Thread(target=press_a)
failsafe_thread = threading.Thread(target=failsafe)

a_thread.start()
failsafe_thread.start()

