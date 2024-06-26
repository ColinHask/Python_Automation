import pyautogui
import keyboard
import time
import os
import cv2

# List of image files for the "X" buttons you want to detect
x_button_images = ['x_button1.png', 'x_button2.png', 'x_button3.png', 'x_button4.png', 'x_button5.png']

def find_and_move_to_x_button():
    """
    Finds any of the "X" buttons on the screen and moves the mouse to it.
    """
    for x_button_image in x_button_images:
        try:
            # Verify the image file exists
            if not os.path.isfile(x_button_image):
                print(f"Error: Image file '{x_button_image}' not found.")
                continue
            
            # Test if the image can be read by OpenCV
            image = cv2.imread(x_button_image)
            if image is None:
                print(f"Failed to load image '{x_button_image}'. It might be corrupted or in an unsupported format.")
                continue

            # Locate the center of the image on the screen
            location = pyautogui.locateCenterOnScreen(x_button_image, confidence=0.9)
            if location is not None:
                pyautogui.moveTo(location)
                print(f"Moved to X button at: {location}")
                return
        except Exception as e:
            print(f"An error occurred with image '{x_button_image}': {e}")
    
    print("No X button found.")

def main():
    """
    Main function to handle the start/stop functionality with the "R" key press.
    """
    running = False
    print("Press 'r' to start/stop the script.")
    
    while True:
        if keyboard.is_pressed('r'):
            running = not running
            if running:
                print("Script started. Press 'r' again to stop.")
            else:
                print("Script stopped. Press 'r' again to start.")
            time.sleep(0.5)  # To prevent multiple toggles from a single press

        if running:
            find_and_move_to_x_button()
            time.sleep(1)  # Adjust the interval as needed to prevent excessive CPU usage

if __name__ == "__main__":
    main()
