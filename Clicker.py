# Clicker
import time
import threading
from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Listener, KeyCode

# Set the number of clicks per second
CPS = 100

# Initialize mouse controller
mouse = MouseController()

# Variables to control the clicker state
clicking = False
running = True

# Define the start/stop key
start_stop_key = KeyCode(char='r')

def click_mouse():
    while running:
        if clicking:
            mouse.click(Button.left, 1)
            time.sleep(1 / CPS)
        else:
            time.sleep(0.1)

def on_press(key):
    global clicking
    if key == start_stop_key:
        clicking = not clicking

def on_release(key):
    # Stop the listener when 'esc' key is pressed
    if key == KeyCode(char='q'):
        global running
        running = False
        return False

click_thread = threading.Thread(target=click_mouse)
click_thread.start()

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
