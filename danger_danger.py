import pyautogui
import keyboard
import random
import time
import string

# Global variable to control the running state
running = False

def random_string(length=10):
    """
    Generate a random string of specified length.
    """
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))

def random_action():
    """
    Performs a random action from the specified list.
    """
    actions = [
        "click_random",
        "double_click_random",
        "type_help_me",
        "type_malice",
        "ctrl_a_ctrl_c",
        "ctrl_v",
        "click_and_drag",
        "move_random_pattern",
        "scroll_random",
        "type_random_string",
        "press_random_key",
        "right_click_random",
        "middle_click_random",
        "highlight_random_text",
        "minimize_all_windows",
        "maximize_all_windows",
        "move_circle",
        "random_move_and_click"
    ]
    action = random.choice(actions)
    
    screen_width, screen_height = pyautogui.size()
    random_x = random.randint(0, screen_width - 1)
    random_y = random.randint(0, screen_height - 1)
    drag_x = random.randint(0, screen_width - 1)
    drag_y = random.randint(0, screen_height - 1)

    if action == "click_random":
        pyautogui.click(random_x, random_y)
    elif action == "double_click_random":
        pyautogui.doubleClick(random_x, random_y)
    elif action == "type_help_me":
        pyautogui.write("HELP ME")
    elif action == "type_malice":
        pyautogui.write("MALICE")
    elif action == "ctrl_a_ctrl_c":
        pyautogui.hotkey("ctrl", "a")
        pyautogui.hotkey("ctrl", "c")
    elif action == "ctrl_v":
        pyautogui.hotkey("ctrl", "v")
    elif action == "click_and_drag":
        pyautogui.moveTo(random_x, random_y)
        pyautogui.dragTo(drag_x, drag_y, duration=0.5)
    elif action == "move_random_pattern":
        pyautogui.moveTo(random_x, random_y)
        for _ in range(10):
            pyautogui.moveTo(random.randint(0, screen_width - 1), random.randint(0, screen_height - 1), duration=0.1)
    elif action == "scroll_random":
        pyautogui.scroll(random.randint(-100, 100))
    elif action == "type_random_string":
        pyautogui.write(random_string())
    elif action == "press_random_key":
        pyautogui.press(random.choice(string.ascii_lowercase))
    elif action == "right_click_random":
        pyautogui.rightClick(random_x, random_y)
    elif action == "middle_click_random":
        pyautogui.middleClick(random_x, random_y)
    elif action == "highlight_random_text":
        pyautogui.moveTo(random_x, random_y)
        pyautogui.dragTo(drag_x, drag_y, button='left', duration=0.5)
    elif action == "minimize_all_windows":
        pyautogui.hotkey("win", "d")
    elif action == "maximize_all_windows":
        pyautogui.hotkey("win", "shift", "m")
    elif action == "move_circle":
        radius = 100
        for i in range(360):
            angle = i * (3.14159 / 180)
            x = int(random_x + radius * pyautogui.cos(angle))
            y = int(random_y + radius * pyautogui.sin(angle))
            pyautogui.moveTo(x, y, duration=0.01)
    elif action == "random_move_and_click":
        for _ in range(10):
            pyautogui.moveTo(random.randint(0, screen_width - 1), random.randint(0, screen_height - 1), duration=0.1)
            pyautogui.click()

def toggle_running(event):
    """
    Toggle the running state when 'r' is pressed.
    """
    global running
    running = not running
    if running:
        print("Script started. Press 'r' again to stop.")
    else:
        print("Script stopped. Press 'r' again to start.")

def main():
    """
    Main function to handle the start/stop functionality with the "R" key press.
    """
    print("Press 'r' to start/stop the script.")
    
    # Set up the keyboard event listener
    keyboard.on_press_key("r", toggle_running)
    
    while True:
        if running:
            random_action()
            time.sleep(0.25)  # Perform a random action pause
        else:
            time.sleep(0.1)  # Sleep briefly to prevent excessive CPU usage when not running

if __name__ == "__main__":
    main()
