import pyautogui
import keyboard
import threading
import time
import os
import tkinter as tk

# Global variables to control the macro state
running = {
    'left_clicker': False,
    'right_clicker': False,
    'mining': False,
    'critical_hit': False,
    'all_disabled': False,
    'left_hold': False,
    'right_hold': False
}
stop_thread = False

def auto_clicker(button, cps):
    """
    Function to handle auto-clicking for the given mouse button.
    """
    global running, stop_thread
    while not stop_thread:
        if running['all_disabled']:
            time.sleep(0.1)
            continue

        if running[f'{button}_clicker']:
            while running[f'{button}_clicker'] and not stop_thread and not running['all_disabled']:
                pyautogui.click(button=button)
                time.sleep(1 / cps)  # Clicks per second
        else:
            time.sleep(0.1)

def critical_hit():
    """
    Function to handle a slower auto-clicking for the left mouse button with additional space tap.
    """
    global running, stop_thread
    while not stop_thread:
        if running['all_disabled']:
            time.sleep(0.1)
            continue

        if running['critical_hit']:
            while running['critical_hit'] and not stop_thread and not running['all_disabled']:
                pyautogui.keyDown('space')  # Press space
                pyautogui.keyUp('space')  # Release space
                time.sleep(0.1)  # Additional wait after space tap
                pyautogui.click(button='left')
                time.sleep(0.4)  # Wait 0.4 seconds between clicks
        else:
            time.sleep(0.1)

def mine():
    """
    Function to handle auto mining by holding the left mouse button.
    """
    global running, stop_thread
    while not stop_thread:
        if running['all_disabled']:
            time.sleep(0.1)
            continue

        if running['mining']:
            # Hold left mouse button to start mining
            pyautogui.mouseDown(button='left')
            while running['mining'] and not stop_thread and not running['all_disabled']:
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
        if running['all_disabled']:
            time.sleep(0.1)
            continue

        if running['mining']:
            pyautogui.keyDown('w')
            while running['mining'] and not stop_thread and not running['all_disabled']:
                time.sleep(0.1)
            pyautogui.keyUp('w')
        else:
            time.sleep(0.1)

def hold_mouse(button):
    """
    Function to hold the specified mouse button.
    """
    global running, stop_thread
    while not stop_thread:
        if running['all_disabled']:
            time.sleep(0.1)
            continue

        if running[f'{button}_hold']:
            pyautogui.mouseDown(button=button)
            while running[f'{button}_hold'] and not stop_thread and not running['all_disabled']:
                time.sleep(0.1)
            pyautogui.mouseUp(button=button)
        else:
            time.sleep(0.1)

def placeholder_thread():
    """
    Placeholder function where additional code can be added to run when the macro is started.
    """
    global running, stop_thread
    while not stop_thread:
        if running['all_disabled']:
            time.sleep(0.1)
            continue

        if any(running.values()):
            # Add code here to run when any macro is started
            print("Placeholder thread running")
            while any(running.values()) and not stop_thread and not running['all_disabled']:
                time.sleep(0.1)
        else:
            time.sleep(0.1)

def toggle_script(key, function_name):
    """
    Function to toggle the macro on and off when the specified key is pressed.
    """
    global running, stop_thread
    while not stop_thread:
        if running['all_disabled']:
            time.sleep(0.1)
            continue

        if keyboard.is_pressed(key):
            running[function_name] = not running[function_name]
            if running[function_name]:
                print(f"{function_name} started")
            else:
                print(f"{function_name} stopped")
            time.sleep(0.5)  # Debounce delay to prevent rapid toggling

def toggle_all_disabled_caps_lock():
    """
    Function to toggle all macros on and off when the 'Caps Lock' key is pressed.
    """
    global running, stop_thread
    while not stop_thread:
        if keyboard.is_pressed('caps lock'):
            running['all_disabled'] = not running['all_disabled']
            if running['all_disabled']:
                print("All macros disabled")
            else:
                print("All macros enabled")
            time.sleep(0.5)  # Debounce delay to prevent rapid toggling

def stop_script():
    """
    Function to stop the entire script safely when the 'ESC' key is pressed.
    """
    keyboard.wait('esc')
    print("Emergency stop activated")
    os._exit(1)

def create_ui():
    """
    Function to create a simple UI displaying the macros and their controls.
    """
    root = tk.Tk()
    root.title("Macro Controls")
    text = tk.Text(root, height=10, width=50)
    text.pack()
    text.insert(tk.END, "Macro Controls:\n")
    text.insert(tk.END, "R: Toggle Left Clicker (60 CPS)\n")
    text.insert(tk.END, "G: Toggle Right Clicker (60 CPS)\n")
    text.insert(tk.END, "H: Toggle Auto Mining\n")
    text.insert(tk.END, "C: Toggle Critical Hit\n")
    text.insert(tk.END, "X: Toggle Left Click Hold\n")
    text.insert(tk.END, "Z: Toggle Right Click Hold\n")
    text.insert(tk.END, "Caps Lock: Disable/Enable Macro keys\n")
    text.insert(tk.END, "ESC: Emergency Stop\n")
    text.config(state=tk.DISABLED)  # Make the text box read-only
    root.mainloop()

if __name__ == "__main__":
    ui_thread = threading.Thread(target=create_ui)
    
    left_clicker_thread = threading.Thread(target=auto_clicker, args=('left', 60))
    right_clicker_thread = threading.Thread(target=auto_clicker, args=('right', 60))
    critical_hit_thread = threading.Thread(target=critical_hit)
    mine_thread = threading.Thread(target=mine)
    walk_forward_thread = threading.Thread(target=walk_forward)
    left_hold_thread = threading.Thread(target=hold_mouse, args=('left',))
    right_hold_thread = threading.Thread(target=hold_mouse, args=('right',))
    placeholder_thread = threading.Thread(target=placeholder_thread)

    toggle_left_clicker_thread = threading.Thread(target=toggle_script, args=('r', 'left_clicker'))
    toggle_right_clicker_thread = threading.Thread(target=toggle_script, args=('g', 'right_clicker'))
    toggle_mine_thread = threading.Thread(target=toggle_script, args=('h', 'mining'))
    toggle_critical_hit_thread = threading.Thread(target=toggle_script, args=('c', 'critical_hit'))
    toggle_left_hold_thread = threading.Thread(target=toggle_script, args=('x', 'left_hold'))
    toggle_right_hold_thread = threading.Thread(target=toggle_script, args=('z', 'right_hold'))
    toggle_all_disabled_thread = threading.Thread(target=toggle_all_disabled_caps_lock)
    stop_script_thread = threading.Thread(target=stop_script)

    ui_thread.start()
    left_clicker_thread.start()
    right_clicker_thread.start()
    critical_hit_thread.start()
    mine_thread.start()
    walk_forward_thread.start()
    left_hold_thread.start()
    right_hold_thread.start()
    placeholder_thread.start()

    toggle_left_clicker_thread.start()
    toggle_right_clicker_thread.start()
    toggle_mine_thread.start()
    toggle_critical_hit_thread.start()
    toggle_left_hold_thread.start()
    toggle_right_hold_thread.start()
    toggle_all_disabled_thread.start()
    stop_script_thread.start()

    ui_thread.join()
    left_clicker_thread.join()
    right_clicker_thread.join()
    critical_hit_thread.join()
    mine_thread.join()
    walk_forward_thread.join()
    left_hold_thread.join()
    right_hold_thread.join()
    placeholder_thread.join()
    toggle_left_clicker_thread.join()
    toggle_right_clicker_thread.join()
    toggle_mine_thread.join()
    toggle_critical_hit_thread.join()
    toggle_left_hold_thread.join()
    toggle_right_hold_thread.join()
    toggle_all_disabled_thread.join()
    stop_script_thread.join()
