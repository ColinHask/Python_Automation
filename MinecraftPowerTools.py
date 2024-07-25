# MinecraftPowerTools

import pyautogui
import keyboard
import threading
import time

# Global variables to control the macro state
running = {
    'left_clicker': False,
    'right_clicker': False,
    'mining': False
}
stop_thread = False

def auto_clicker(button):
    """
    Function to handle auto-clicking for the given mouse button.
    """
    global running, stop_thread
    while not stop_thread:
        if running[f'{button}_clicker']:
            while running[f'{button}_clicker']:
                pyautogui.click(button=button)
                time.sleep(1 / 60)  #  clicks per second
        else:
            time.sleep(0.1)

def mine():
    """
    Function to handle auto mining by holding the left mouse button.
    """
    global running, stop_thread
    while not stop_thread:
        if running['mining']:
            # Hold left mouse button to start mining
            pyautogui.mouseDown(button='left')
            while running['mining']:
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
        if running['mining']:
            pyautogui.keyDown('w')
            while running['mining']:
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
        if any(running.values()):
            # Add code here to run when any macro is started
            print("Placeholder thread running")
            while any(running.values()):
                time.sleep(0.1)
        else:
            time.sleep(0.1)

def toggle_script(key, function_name):
    """
    Function to toggle the macro on and off when the specified key is pressed.
    """
    global running, stop_thread
    while not stop_thread:
        if keyboard.is_pressed(key):
            running[function_name] = not running[function_name]
            if running[function_name]:
                print(f"{function_name} started")
            else:
                print(f"{function_name} stopped")
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
    left_clicker_thread = threading.Thread(target=auto_clicker, args=('left',))
    right_clicker_thread = threading.Thread(target=auto_clicker, args=('right',))
    mine_thread = threading.Thread(target=mine)
    walk_forward_thread = threading.Thread(target=walk_forward)
    placeholder_thread = threading.Thread(target=placeholder_thread)

    toggle_left_clicker_thread = threading.Thread(target=toggle_script, args=('r', 'left_clicker'))
    toggle_right_clicker_thread = threading.Thread(target=toggle_script, args=('g', 'right_clicker'))
    toggle_mine_thread = threading.Thread(target=toggle_script, args=('h', 'mining'))
    stop_script_thread = threading.Thread(target=stop_script)

    left_clicker_thread.start()
    right_clicker_thread.start()
    mine_thread.start()
    walk_forward_thread.start()
    placeholder_thread.start()

    toggle_left_clicker_thread.start()
    toggle_right_clicker_thread.start()
    toggle_mine_thread.start()
    stop_script_thread.start()

    left_clicker_thread.join()
    right_clicker_thread.join()
    mine_thread.join()
    walk_forward_thread.join()
    placeholder_thread.join()
    toggle_left_clicker_thread.join()
    toggle_right_clicker_thread.join()
    toggle_mine_thread.join()
    stop_script_thread.join()
