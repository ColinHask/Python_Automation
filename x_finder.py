import pyautogui
import keyboard
import time
import os
import cv2

# List of image files for the "X" buttons you want to detect
x_button_images = ['x_button1.png', 'x_button2.png', 'x_button3.png', 'x_button4.png', 'x_button5.png']

running = False  # Global variable to control the running state

def find_and_move_to_x_button():
    """
    Finds any of the "X" buttons on the screen, moves the mouse to it, and clicks.
    """
    for x_button_image in x_button_images:
        try:
            # Verify the image file exists
            image_path = os.path.abspath(x_button_image)
            if not os.path.isfile(image_path):
                print(f"Error: Image file '{x_button_image}' not found at {image_path}.")
                continue
            
            print(f"Attempting to load image '{x_button_image}' from '{image_path}'")
            
            # Test if the image can be read by OpenCV
            image = cv2.imread(image_path)
            if image is None:
                print(f"Failed to load image '{x_button_image}'. It might be corrupted or in an unsupported format.")
                continue
            else:
                print(f"Successfully loaded image '{x_button_image}'.")

            # Locate the center of the image on the screen
            location = pyautogui.locateCenterOnScreen(image_path, confidence=0.6)
            if location is not None:
                pyautogui.moveTo(location)
                pyautogui.click()
                print(f"Moved to and clicked X button at: {location}")
                return
            else:
                print(f"X button image '{x_button_image}' not found on screen.")
        except Exception as e:
            print(f"An error occurred with image '{x_button_image}': {str(e)}")
    
    print("No X button found.")

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
            find_and_move_to_x_button()
            time.sleep(0.025)  # Adjust the interval as needed to prevent excessive CPU usage
        else:
            time.sleep(0.1)  # Sleep briefly to prevent excessive CPU usage when not running

if __name__ == "__main__":
    main()
