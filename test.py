# _____________________________WORKING CODE USING LOOP _________________________________
# ****************************************************************************************
# *****************************************************************************************

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set the URL of the meeting
meeting_url = "https://jiomeetpro.jio.com/shortener?meetingId=7863373088&pwd=7Fte4"

# Set the number of guest users to simulate
num_users = 50

# Set the path to the Chrome webdriver
webdriver_path = r"C:\Users\Saurabh16.Yadav\Desktop\jiomeet\chromedriver.exe"

# Set up the browser driver
driver_options = webdriver.ChromeOptions()
driver_options.add_argument('--headless')
driver_options.add_argument("--use-fake-ui-for-media-stream")
driver_options.add_argument("--use-fake-device-for-media-stream")
driver_options.add_argument("--disable-extensions")
driver_options.add_argument("--disable-gpu")

# Create a list to store the driver instances
drivers = []

# Calculate the number of windows required
num_windows = -(-num_users // 15)  # Round up division

try:
    for i in range(num_windows):
        # Open a new browser window
        driver = webdriver.Chrome(options=driver_options)
        drivers.append(driver)

        # Open 15 tabs in the window and join the meeting
        for j in range(15):
            # Open a new tab
            driver.execute_script("window.open('about:blank', '_blank');")
            driver.switch_to.window(driver.window_handles[j + 1])

            # Join the meeting in the tab
            driver.get(meeting_url)

            name_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "name")))
            name_field.clear()
            name_field.send_keys(f"Guest User {i * 15 + j + 1}")

            join_button = driver.find_element(By.XPATH, "//button[@type='submit']")
            join_button.click()

    # Stay in the meeting indefinitely without refreshing
    while True:
        pass

finally:
    # Close all browser windows and quit the drivers
    for driver in drivers:
        driver.quit()
# ******************************************************************************************************
# *******************************************************************************************************
# ________________________________________________________________________________________________________