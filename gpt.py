# gpt

import pyautogui
import time
import pyperclip

# Method to be modified by ChatGPT
def updatable_method():
    print("This is the original functionality.")

# Method to update the updatable_method using ChatGPT
def update_method():
    # Open the browser and navigate to ChatGPT
    pyautogui.hotkey('ctrl', 't')  # Open a new tab
    time.sleep(1)
    pyautogui.write('https://chat.openai.com/chat')
    pyautogui.press('enter')
    time.sleep(10)  # Adjust based on load time and login requirement

    # Input prompt to ChatGPT
    prompt = """
    Update the following Python method to print 'This is the updated functionality.':
    
    def updatable_method():
        print("This is the original functionality.")
    """
    pyperclip.copy(prompt)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')

    # Wait for the response
    time.sleep(10)  # Adjust based on response time

    # Copy the response (assuming the response box is focused)
    pyautogui.hotkey('ctrl', 'a')  # Select all text
    pyautogui.hotkey('ctrl', 'c')  # Copy to clipboard

    # Retrieve the copied text from the clipboard
    updated_code = pyperclip.paste()

    # Replace the method in this script
    script_file = __file__
    with open(script_file, 'r') as file:
        lines = file.readlines()

    # Find the start and end lines of the updatable_method
    start_index = None
    end_index = None
    for i, line in enumerate(lines):
        if 'def updatable_method' in line:
            start_index = i
        if start_index is not None and line.strip() == '':
            end_index = i
            break

    # Replace the old method with the updated code
    if start_index is not None and end_index is not None:
        updated_code_lines = updated_code.split('\n')
        lines = lines[:start_index] + updated_code_lines + lines[end_index+1:]

    # Write the updated lines back to the file
    with open(script_file, 'w') as file:
        file.writelines(lines)

    print("Method updated successfully!")

# Call the update_method function
if __name__ == "__main__":
    # Uncomment the next line to run the update method
    # update_method()
    
    # Test the updatable_method
    updatable_method()

