import time
import threading
from pynput.mouse import Button, Controller as MouseController
import tkinter as tk

# Set the number of clicks per second
CPS = 100

# Initialize mouse controller
mouse = MouseController()

# Variables to control the clicker state
clicking = False
running = True

def click_mouse():
    while running:
        if clicking:
            mouse.click(Button.left, 1)
            time.sleep(1 / CPS)
        else:
            time.sleep(0.1)

def start_clicking():
    global clicking
    clicking = True

def stop_clicking():
    global clicking
    clicking = False

# Thread to handle the mouse clicking
click_thread = threading.Thread(target=click_mouse)
click_thread.start()

# Create a simple Tkinter GUI
root = tk.Tk()
root.title("Auto Clicker")
root.geometry("400x200")  # Set the window size to 400x200

start_button = tk.Button(root, text="Start Clicking", command=start_clicking)
start_button.pack(pady=10)

stop_button = tk.Button(root, text="Stop Clicking", command=stop_clicking)
stop_button.pack(pady=10)

# Function to stop the program when the GUI is closed
def on_closing():
    global running
    running = False
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
