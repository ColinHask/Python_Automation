import pyautogui
import keyboard
import threading
import time
import os

# List of image files to detect and click
image_files = [
    'detect1.png',
    'detect2.png',
    'detect3.png',
    'detect4.png',
    'detect5.png',
    'detect6.png',
    'detect7.png'
    # Add more images as needed
]

# Global variable to control the running state
running = False

def detect_and_click_images():
    """
    Detects the specified images on the screen, moves the mouse to their locations,
    and performs a single click.
    """
    for image in image_files:
        image_path = os.path.abspath(image)
        if not os.path.isfile(image_path):
            print(f"Error: Image file '{image_path}' not found.")
            continue

        try:
            location = pyautogui.locateCenterOnScreen(image_path, confidence=0.9)
            if location is not None:
                pyautogui.moveTo(location)
                pyautogui.click()
                print(f"Clicked on image '{image_path}' at {location}.")

                # Custom extra steps after clicking specific images
                if image == 'detect4.png':
                    pyautogui.write(r"Hello beautiful girlfriend!")
                    print("Typed 'AUTO EMAIL' after clicking detect5.png")
                elif image == 'detect5.png':
                    pyautogui.write("bmunn3@students.kennesaw.edu")
                    print("Typed 'bmunn3@students.kennesaw.edu' after clicking detect5.png")
                elif image == 'detect6.png':
                    pyautogui.write("I love you <3")
                    print("Typed 'I love you <3' after clicking detect5.png")
                
            else:
                print(f"Image '{image_path}' not found on screen.")
        except Exception as e:
            print(f"An error occurred with image '{image_path}': {str(e)}")

def detect_and_click_loop():
    """
    The loop that continuously detects and clicks images when running is True.
    """
    while True:
        if running:
            detect_and_click_images()
            time.sleep(1)  # Wait for 1 second before checking again
        else:
            time.sleep(0.1)  # Sleep briefly to prevent excessive CPU usage when not running

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

    # Start the detection and clicking loop in a separate thread
    thread = threading.Thread(target=detect_and_click_loop)
    thread.daemon = True
    thread.start()

    # Keep the main thread alive to listen for the 'r' key press
    keyboard.wait('esc')  # Press 'esc' to exit the script

if __name__ == "__main__":
    main()
