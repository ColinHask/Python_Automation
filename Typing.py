import tkinter as tk  # Import the tkinter library for GUI creation
import pyautogui  # Import the PyAutoGUI library for automating GUI interactions
import time  # Import the time library for time-related functions
import threading  # Import the threading library to run tasks concurrently

def type_text(text, speed):
    """
    Types out the given text at the specified speed.

    :param text: The text to be typed.
    :param speed: The time interval (in seconds) between each keystroke.
    """
    for char in text:
        pyautogui.typewrite(char)  # Type each character
        time.sleep(speed)  # Wait for the specified time interval between keystrokes

def countdown(count):
    """
    Updates the countdown label every second and starts typing when the countdown reaches zero.

    :param count: The current countdown number.
    """
    if count > 0:
        countdown_label.config(text=str(count))  # Update the countdown label with the current count
        root.after(1000, countdown, count - 1)  # Call this function again after 1 second with count decremented by 1
    else:
        countdown_label.config(text="Typing...")  # Update the label to indicate typing is about to start
        time.sleep(1)  # Small delay before starting typing
        type_text(text_to_type, typing_speed)  # Call the type_text function to start typing the text
        root.destroy()  # Close the GUI window after typing is complete

# Example usage variables:
text_to_type = "Automation using Python is a powerful way to streamline repetitive tasks and increase efficiency. By utilizing libraries such as PyAutoGUI, developers can programmatically control the mouse and keyboard to perform a variety of actions, such as typing, clicking, and moving the cursor. This allows for the automation of tasks like data entry, web navigation, and GUI interactions. Additionally, incorporating GUI elements with the Tkinter library enables the creation of user-friendly interfaces to control these automated processes. This combination of automation and user interfaces can significantly reduce the manual effort required for routine operations, making it an invaluable tool for productivity enhancement."  # The text to be typed out
typing_speed = 0.00005# The typing speed in seconds per character 

# Create the main GUI window
root = tk.Tk()  # Initialize the tkinter window
root.title("Countdown Timer")  # Set the window title

# Create and pack the countdown label
countdown_label = tk.Label(root, font=('Helvetica', 48))  # Create a label with a large font for the countdown
countdown_label.pack(pady=20)  # Add padding around the label

# Create and pack the start button
start_button = tk.Button(root, text="Start", command=lambda: countdown(5))  # Create a button that starts the countdown from 5 seconds
start_button.pack(pady=20)  # Add padding around the button

root.mainloop()  # Start the tkinter event loop to run the GUI
