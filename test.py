from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

# Set the URL of the meeting
meeting_url = "https://jiomeetpro.jio.com/shortener?meetingId=5200362798&pwd=rtHt3"

# Set the number of guest users to simulate
num_users = 1

# Set the path to the Chrome webdriver (you can use other browsers as well)
webdriver_path = r"C:\Users\Saurabh16.Yadav\Desktop\jiomeet\chromedriver.exe"

# Set up the browser options
options = Options()
# options.add_argument("--headless")      # Run in headless mode, no browser window will be opened
options.add_argument("--use-fake-ui-for-media-stream")  # Grant permission without user prompt
options.add_argument("--use-fake-device-for-media-stream")  # Use fake device for media streams

# Set up the browser driver
driver = webdriver.Chrome( options=options)

try:
    # Open the initial browser window
    driver.get(meeting_url)

    # Wait for the meeting join page to load
    WebDriverWait(driver, 10).until(EC.title_contains("JioMeet"))

    for i in range(num_users):
        # Open a new browser window
        driver.execute_script("window.open('about:blank', 'new_window')")

    # Switch to the new windows if they exist
    if len(driver.window_handles) >= num_users + 1:
        for i in range(1, num_users + 1):
            driver.switch_to.window(driver.window_handles[i])

            # Navigate to the meeting URL
            driver.get(meeting_url)

            try:
                # Wait for the meeting join page to load
                WebDriverWait(driver, 20).until(EC.title_contains("JioMeet"))

                # Simulate entering the user's name as a guest
                name_field = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "name")))
                name_field.clear()
                name_field.send_keys(f"Guest User {i}")

                # Click the join button to join the meeting
                join_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/app-root/div/div/div[2]/div/app-join-call/div[1]/div/div[3]/div[2]/div/div/section/form/div[4]")))
                join_button.click()

                # Wait for the meeting to run (you can add additional logic here, e.g., waiting for specific elements)
                WebDriverWait(driver, 60).until(EC.title_contains("JioMeet"))

                # Perform additional actions or interactions within the meeting as needed

            except Exception as e:
                print(f"Error occurred for user {i}: {str(e)}")
    else:
        print("Not enough windows available for users")

finally:
    # Close all browser windows and quit the driver
    driver.quit()
