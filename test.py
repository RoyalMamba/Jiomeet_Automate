import concurrent.futures
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MeetingSimulator:
    def __init__(self, meeting_url, num_users, webdriver_path):
        self.meeting_url = meeting_url
        self.num_users = num_users
        self.webdriver_path = webdriver_path
        self.drivers = []
        self.options = self._setup_driver_options()
    
    def _setup_driver_options(self):
        options = webdriver.ChromeOptions()
        # options.add_argument('--headless')
        options.add_argument("--use-fake-ui-for-media-stream")
        options.add_argument("--use-fake-device-for-media-stream")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-gpu")
        return options
    
    def join_meeting(self, driver, driver_index):
        handles = driver.window_handles
        
        for user in range(1, len(handles) + 1):
            driver.switch_to.window(driver.window_handles[user])

            name = f"Guest User {user + driver_index * 15}"
            name_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "name")))
            name_field.clear()
            name_field.send_keys(name)

            join_button = driver.find_element(By.XPATH, "//button[@type='submit']")
            join_button.click()
        
        while True:
            pass
    
    def simulate(self):
        # Open the main browser window
        main_driver = webdriver.Chrome(options=self.options)
        self.drivers.append(main_driver)
        main_driver.get(self.meeting_url)

        # Open tabs in each window and join the meeting in parallel
        with concurrent.futures.ThreadPoolExecutor() as executor:
            for i in range(0, self.num_users, 15):
                # Open a new window
                driver = webdriver.Chrome(options=self.options)
                self.drivers.append(driver)

                # Calculate the number of users for this iteration
                num_users_current = min(15, self.num_users - i)

                # Open new tabs in the window and visit the meeting URL
                for _ in range(num_users_current):
                    driver.execute_script(f"window.open('{self.meeting_url}', '_blank');")

                # Execute the join operation in parallel
                futures = [executor.submit(self.join_meeting, driver, driver_index) for driver_index, driver in enumerate(self.drivers)]

        # Stay in the meeting indefinitely without refreshing
        while True:
            pass
    
    def cleanup(self):
        for driver in self.drivers:
            driver.quit()

# Set the URL of the meeting
meeting_url = "https://jiomeetpro.jio.com/shortener?meetingId=2066439537&pwd=wsC71"

# Set the number of guest users to simulate
num_users = 50

# Set the path to the Chrome webdriver
webdriver_path = r"C:\Users\Saurabh16.Yadav\Desktop\jiomeet\chromedriver.exe"

# Create an instance of MeetingSimulator and simulate the meeting
simulator = MeetingSimulator(meeting_url, num_users, webdriver_path)
try:
    simulator.simulate()
except Exception as e:
    print(f"An error occurred: {str(e)}")
finally:
    simulator.cleanup()
