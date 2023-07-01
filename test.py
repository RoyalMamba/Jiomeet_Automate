from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.Edge.options import Options
from selenium.webdriver import EdgeOptions

import time

# Set the URL of the meeting
meeting_url = "https://jiomeetpro.jio.com/shortener?meetingId=0018721439&pwd=C9Cmk"

# Set the number of guest users to simulate
num_users = 50

# Set the path to the Chrome webdriver (you can use other browsers as well)
webdriver_path = r"C:\Users\Saurabh16.Yadav\Desktop\jiomeet\chromedriver.exe"

# Set up the browser options
options = Options()
# options.add_argument("--headless")      # Run in headless mode, no browser window will be opened
options.add_argument("--use-fake-ui-for-media-stream")  # Grant permission without user prompt
options.add_argument("--use-fake-device-for-media-stream")  # Use fake device for media streams
options.add_argument("--disable-extensions")  # Disable extensions to save resources
options.add_argument("--disable-gpu")  # Disable GPU to save resources


# _______________________________EDGE_PERMISSIONS________________________________
# op = webdriver.EdgeOptions()
# op.add_argument('headless')
# op.add_argument("allow-file-access-from-files")
# op.add_argument("use-fake-device-for-media-stream")
# op.add_argument("use-fake-ui-for-media-stream")
# op.add_argument("--disable-features=EnableEphemeralFlashPermission")
# op.add_argument('--disable-notifications')
# op.add_argument('--disable-extensions')
# op.add_argument("--disable-extensions")  # Disable extensions to save resources
# op.add_argument("--disable-gpu")  # Disable GPU to save resources


# profile = {
#     'profile.default_content_setting_values.media_stream_mic' : 1 ,
#     'profile.default_content_setting_values.media_stream_camera' : 1,
# }

# op.add_experimental_option('prefs', profile)
# driver = webdriver.Edge(options = op)

# _______________________________________________________________________________

# Set up the browser driver
driver = webdriver.Chrome(options=options)

# driver.maximize_window()
try:
    # Open the initial browser window and join the meeting
    driver.get(meeting_url)

    # Fill in the form and click the join button
    for i in range(num_users):
        # Wait for the meeting join page to load
        WebDriverWait(driver, 20).until(EC.title_contains("JioMeet"))

        # Simulate entering the user's name as a guest
        name_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "name")))
        name_field.clear()
        name_field.send_keys(f"Guest User {i}")

        # Click the join button to join the meeting
        join_button = driver.find_element(By.XPATH, "//button[@type='submit']")
        join_button.click()

        # Open a new tab for the next user
        if i < num_users - 1:
            driver.execute_script("window.open();")  # Open a new tab
            driver.switch_to.window(driver.window_handles[i + 1])  # Switch to the new tab
            driver.get(meeting_url)  # Load the meeting URL

    # Stay in the meeting indefinitely without refreshing
    while True:
        time.sleep(10)  # Sleep for an interval to keep the script running

finally:
    # Close all browser windows and quit the driver
    driver.quit()
