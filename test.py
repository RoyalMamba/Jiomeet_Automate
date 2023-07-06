import concurrent.futures
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# import logging 

# # logging.basicConfig(filename='jiomeet_stress.log')

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
        
        for user in range(len(handles)):
            try :
                driver.switch_to.window(driver.window_handles[user])
<<<<<<< HEAD
                name = f"Guest User {(user-1) + driver_index *6}"
=======
                name = f"Guest User {(user-1) + driver_index *5}"
>>>>>>> 8f0dd104a3413d8d0fc387de9ccf8969c483a2e9
                name_field = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "name")))
                name_field.clear()
                name_field.send_keys(name)

                join_button = driver.find_element(By.XPATH, "//button[@type='submit']")
                join_button.click()
            except:
                pass 
        return driver
        
    def switch_meetings(self, driver):
        handles = driver.window_handles
        for handle in handles:
            driver.switch_to.window(handle)
            try:
                info = driver.find_element(By.XPATH, '/html/body/div[1]/app-root/div/div/div/div/app-conference/app-call/div[1]/div/div[1]/div[2]/app-call-controls-v3/div[1]/div[1]/div/div/div/div[2]/app-call-info-v2/div[1]')
                info.click()
            except:
                pass           
    
    def simulate(self):
        # # Open the main browser window
        # main_driver = webdriver.Chrome(options=self.options)
        # self.drivers.append(main_driver)
        # main_driver.get(self.meeting_url)

        # Open tabs in each window and join the meeting in parallel
        with concurrent.futures.ThreadPoolExecutor() as executor:
            windows = 0
            futures = []
<<<<<<< HEAD
            for i in range(0, self.num_users,6):
=======
            for i in range(0, self.num_users,5):
>>>>>>> 8f0dd104a3413d8d0fc387de9ccf8969c483a2e9
                # Open a new window
                driver = webdriver.Chrome(options=self.options)
                self.drivers.append(driver)

                # Calculate the number of users for this iteration
<<<<<<< HEAD
                num_users_current = min(6, self.num_users - i)
=======
                num_users_current = min(5, self.num_users - i)
>>>>>>> 8f0dd104a3413d8d0fc387de9ccf8969c483a2e9

                # Open new tabs in the window and visit the meeting URL
                for _ in range(num_users_current):
                    driver.execute_script(f"window.open('{self.meeting_url}', '_blank');")

                # Execute the join operation in parallel
                future = executor.submit(self.join_meeting, driver, windows)
                futures.append(future)
                windows+=1 
<<<<<<< HEAD
            
        while True:
            # for future in concurrent.futures.as_completed(futures):
            #     executedDriver = future.result()
            #     # self.switch_meetings(executedDriver)
            #     executor.submit(self.switch_meetings, executedDriver)
            with concurrent.futures.ThreadPoolExecutor() as executor:
                keep_alive_future = [executor.submit(self.switch_meetings,future.result()) for future in concurrent.futures.as_completed(futures)]
                concurrent.futures.wait(futures)
=======
                
            while True:
                for future in concurrent.futures.as_completed(futures):
                    executedDriver = future.result()
                    # self.switch_meetings(executedDriver)
                    executor.submit(self.switch_meetings, executedDriver)

>>>>>>> 8f0dd104a3413d8d0fc387de9ccf8969c483a2e9

        # Stay in the meeting indefinitely without refreshing
    def cleanup(self):
        for driver in self.drivers:
            driver.quit()

# Set the URL of the meeting
meeting_url = input('Enter the link: ')

# Set the number of guest users to simulate
<<<<<<< HEAD
num_users = 12
=======
num_users = 36
>>>>>>> 8f0dd104a3413d8d0fc387de9ccf8969c483a2e9

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
