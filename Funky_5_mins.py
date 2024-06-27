# Funky_5_mins

import webbrowser
import time
import pyautogui
import subprocess



# URL of the YouTube video
youtube_url = 'https://www.youtube.com/watch?v=poa_QBvtIBA'

# Function to open the YouTube link
def open_youtube_link():
    webbrowser.open(youtube_url)
    print(f"Opened YouTube link: {youtube_url}")

def message():
    # Open Notepad
    subprocess.Popen('notepad.exe')

    # Wait for Notepad to open
    time.sleep(2)

    # Type "get funky"
    pyautogui.write('get funky', interval=0.1)

# Main loop to open the link every 5 minutes
while True:
    time.sleep(150)
    message()
    time.sleep(3)
    open_youtube_link()
    
