from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# Path to your WebDriver (e.g., ChromeDriver)
driver_path = 'path/to/chromedriver'

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(driver_path)

try:
    # Open YouTube
    driver.get("https://www.youtube.com")

    # Wait for the page to load
    time.sleep(5)

    # Find the search box
    search_box = driver.find_element(By.NAME, 'search_query')

    # Type the search term
    search_term = 'Python programming'
    search_box.send_keys(search_term)

    # Press Enter to search
    search_box.send_keys(Keys.RETURN)

    # Wait for the search results to load
    time.sleep(5)

    # Find the first video in the search results
    first_video = driver.find_element(By.XPATH, '//*[@id="video-title"]')

    # Click on the first video
    first_video.click()

    # Wait for the video page to load
    time.sleep(5)

    # Perform some navigation functions (e.g., pause the video)
    video_player = driver.find_element(By.CLASS_NAME, 'video-stream')
    actions = ActionChains(driver)
    actions.move_to_element(video_player).click().perform()

    # Pause the video
    video_player.send_keys(Keys.SPACE)

    # Wait for a few seconds
    time.sleep(5)

finally:
    # Close the browser
    driver.quit()
