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
    Performs a random action from the specified list with a 25% chance of clicking each time.
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
        "random_move_and_click",
        "print_file",
        "new_tab",
        "close_tab",
        "switch_tabs",
        "refresh_page",
        "open_task_manager",
        "open_file_explorer",
        "find_text",
        "open_emoji_panel"
    ]
    
    screen_width, screen_height = pyautogui.size()
    random_x = random.randint(0, screen_width - 1)
    random_y = random.randint(0, screen_height - 1)
    drag_x = random.randint(0, screen_width - 1)
    drag_y = random.randint(0, screen_height - 1)

    # 25% chance to perform a clicking action
    if random.random() < 0.25:
        action = random.choice(actions[:8])  # Select from clicking-related actions
    else:
        action = random.choice(actions[8:])  # Select from other actions

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
    elif action == "random_move_and_click":
        for _ in range(10):
            pyautogui.moveTo(random.randint(0, screen_width - 1), random.randint(0, screen_height - 1), duration=0.1)
            pyautogui.click()
    elif action == "print_file":
        pyautogui.hotkey("ctrl", "p")
    elif action == "new_tab":
        pyautogui.hotkey("ctrl", "t")
    elif action == "close_tab":
        pyautogui.hotkey("ctrl", "w")
    elif action == "switch_tabs":
        pyautogui.hotkey("ctrl", "tab")
    elif action == "refresh_page":
        pyautogui.hotkey("f5")
    elif action == "open_task_manager":
        pyautogui.hotkey("ctrl", "shift", "esc")
    elif action == "open_file_explorer":
        pyautogui.hotkey("win", "e")
    elif action == "find_text":
        pyautogui.hotkey("ctrl", "f")
    elif action == "open_emoji_panel":
        pyautogui.hotkey("win", ".")

def toggle_running():
    """
    Toggle the running state.
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
    
    # Set up the keyboard event listener for 'r' key
    keyboard.add_hotkey('r', toggle_running)
    
    while True:
        if running:
            random_action()
            time.sleep(0.25)  # Perform a random action every half second
        else:
            time.sleep(0.1)  # Sleep briefly to prevent excessive CPU usage when not running

if __name__ == "__main__":
    main()
