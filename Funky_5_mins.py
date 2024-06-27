# Funky_5_mins
import webbrowser
import time
import tkinter as tk
from threading import Timer

import webbrowser
import time
import pyautogui
from threading import Timer

# URL of the YouTube video
youtube_url = 'https://www.youtube.com/watch?v=poa_QBvtIBA'

# Function to open the YouTube link
def open_youtube_link():
    webbrowser.open(youtube_url)
    print(f"Opened YouTube link: {youtube_url}")

# Function to show the popup message
def show_popup():
    pyautogui.alert(text='Get funky!', title='Reminder', button='OK')
    time.sleep(10)  # Wait for 10 seconds before opening the link
    open_youtube_link()

# Main loop to open the link every 5 minutes
while True:
    # Show the popup 10 seconds before opening the link
    Timer(290, show_popup).start()
    # Wait for 5 minutes (300 seconds) before showing the next popup
    time.sleep(300)
