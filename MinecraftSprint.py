import pyautogui
import keyboard
import threading
import time

# Global variables to control the macro state
running = False
stop_thread = False

def press_w():
    """
    Function to handle pressing and holding the 'W' key for moving forward and sprinting.
    """
    global running, stop_thread
    while not stop_thread:
        if running:
            # Tap W
            pyautogui.press('w')
            time.sleep(0.25)
            # Hold W and start sprinting
            pyautogui.keyDown('w')
            pyautogui.keyDown('ctrl')
            while running:
                time.sleep(0.1)
            # Release keys when stopping
            pyautogui.keyUp('w')
            pyautogui.keyUp('ctrl')
        else:
            time.sleep(0.1)

def jump():
    """
    Function to handle pressing the space bar to jump every 0.3 seconds.
    """
    global running, stop_thread
    while not stop_thread:
        if running:
            while running:
                pyautogui.press('space')
                time.sleep(0.3)  # Time between jumps (adjustable)
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
    # Creating and starting threads for each function
    press_w_thread = threading.Thread(target=press_w)
    jump_thread = threading.Thread(target=jump)
    placeholder_thread = threading.Thread(target=placeholder_thread)
    toggle_script_thread = threading.Thread(target=toggle_script)
    stop_script_thread = threading.Thread(target=stop_script)

    press_w_thread.start()
    jump_thread.start()
    placeholder_thread.start()
    toggle_script_thread.start()
    stop_script_thread.start()

    # Waiting for all threads to complete (which in this case, they run indefinitely)
    press_w_thread.join()
    jump_thread.join()
    placeholder_thread.join()
    toggle_script_thread.join()
    stop_script_thread.join()
