import pyautogui
import keyboard
import threading
import time

# Global variables to control the macro state
running = False
stop_thread = False

def mine():
    """
    Function to handle auto mining by holding the left mouse button.
    """
    global running, stop_thread
    while not stop_thread:
        if running:
            # Hold left mouse button to start mining
            pyautogui.mouseDown(button='left')
            while running:
                time.sleep(0.1)
            # Release left mouse button to stop mining
            pyautogui.mouseUp(button='left')
        else:
            time.sleep(0.1)

def walk_forward():
    """
    Function to handle walking forward by holding the 'W' key.
    """
    global running, stop_thread
    while not stop_thread:
        if running:
            pyautogui.keyDown('w')
            while running:
                time.sleep(0.1)
            pyautogui.keyUp('w')
        else:
            time.sleep(0.1)

def placeholder_thread():
    """
    Placeholder function where additional code can be added to run when the macro is started.
    """
    global running, stop_thread
    while not stop_thread:
        if running:
            # Add code here to run when the macro is started
            print("Placeholder thread running")
            while running:
                time.sleep(0.1)
        else:
            time.sleep(0.1)

def toggle_script():
    """
    Function to toggle the macro on and off when the 'R' key is pressed.
    """
    global running, stop_thread
    while not stop_thread:
        if keyboard.is_pressed('r'):
            running = not running
            if running:
                print("Script started")
            else:
                print("Script stopped")
            time.sleep(0.5)  # Debounce delay to prevent rapid toggling

def stop_script():
    """
    Function to stop the entire script safely when the 'ESC' key is pressed.
    """
    global stop_thread
    keyboard.wait('esc')
    stop_thread = True
    print("Script terminated")

if __name__ == "__main__":
    mine_thread = threading.Thread(target=mine)
    walk_forward_thread = threading.Thread(target=walk_forward)
    placeholder_thread = threading.Thread(target=placeholder_thread)
    toggle_script_thread = threading.Thread(target=toggle_script)
    stop_script_thread = threading.Thread(target=stop_script)

    mine_thread.start()
    walk_forward_thread.start()
    placeholder_thread.start()
    toggle_script_thread.start()
    stop_script_thread.start()

    mine_thread.join()
    walk_forward_thread.join()
    placeholder_thread.join()
    toggle_script_thread.join()
    stop_script_thread.join()
