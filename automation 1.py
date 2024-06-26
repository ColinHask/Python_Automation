# automation 1

import pyautogui
import time

def type_text(text, speed):
    """
    Types out the given text at the specified speed.

    :param text: The text to be typed.
    :param speed: The time interval (in seconds) between each keystroke.
    """
    for char in text:
        pyautogui.typewrite(char)
        time.sleep(speed)

# Example usage:
text_to_type = "Hello, this is an automated typing test."
typing_speed = 0.1  # 100 milliseconds per character

# Give yourself a few seconds to focus the desired typing area
print("You have 5 seconds to focus the typing area...")
time.sleep(5)

type_text(text_to_type, typing_speed)
