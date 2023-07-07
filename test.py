import concurrent.futures
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import keyboard
import logging
import time

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s", filename="jiomeet_automate.log")

class MeetingSimulator:
    def __init__(self, meeting_url, num_users, webdriver_path):
        self.meeting_url = meeting_url
        self.num_users = num_users
        self.webdriver_path = webdriver_path
        self.drivers = []
        self.options = self._setup_driver_options()
        self.terminate_automation = False
    
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
        
        for user, handle in enumerate(handles[1:]):
            try:
                driver.switch_to.window(handle)
                name = f"Guest User {((user-1) + driver_index *maximum_tabs)+2}"
                name_field = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "name")))
                name_field.clear()
                name_field.send_keys(name)

                join_button = driver.find_element(By.XPATH, "//button[@type='submit']")
                join_button.click()
                logging.info(f"User {name} joined the meeting successfully.")
                tab_name = name[6:]
                driver.execute_script(f"document.title = '{tab_name}'")
            except Exception as e:
                # logging.error(f"An error occurred while joining the meeting: {str(e)}", exc_info=True)
                logging.warning(f"An error occurred while joining the meeting: Failed to join {name}")

        return driver,driver_index
        
    def switch_meetings(self, driver, driver_index):
        handles = driver.window_handles
        for handleindex, handle in enumerate(handles[1:]):
            driver.switch_to.window(handle)
            try:
                info = driver.find_element(By.XPATH, '/html/body/div[1]/app-root/div/div/div/div/app-conference/app-call/div[1]/div/div[1]/div[2]/app-call-controls-v3/div[1]/div[1]/div/div/div/div[2]/app-call-info-v2/div[1]')
                info.click()
            except:
                logging.warning(f'Unable to find the element in window: {driver_index} Tab: {handleindex+1}')          
    
    def simulate(self):
        # # Open the main browser window
        # main_driver = webdriver.Chrome(options=self.options)
        # self.drivers.append(main_driver)
        # main_driver.get(self.meeting_url)

        # Open tabs in each window and join the meeting in parallel
        with concurrent.futures.ThreadPoolExecutor() as executor:
            windows = 0
            futures = []
            for i in range(0, self.num_users,maximum_tabs):
                # Open a new window
                driver = webdriver.Chrome(options=self.options)
                self.drivers.append(driver)
                logging.info("New browser window opened.")

                # Calculate the number of users for this iteration
                num_users_current = min(maximum_tabs, self.num_users - i)

                # Open new tabs in the window and visit the meeting URL
                for _ in range(num_users_current):
                    driver.execute_script(f"window.open('{self.meeting_url}', '_blank');")
                logging.info(f"{num_users_current} tabs opened in the browser window: {windows}")

                # Execute the join operation in parallel
                future = executor.submit(self.join_meeting, driver, windows)
                futures.append(future)
                windows+=1 

        keyboard.add_hotkey('esc', self.terminate_simulation) 
        while not self.terminate_automation:
            # for future in concurrent.futures.as_completed(futures):
            #     executedDriver = future.result()
            #     # self.switch_meetings(executedDriver)
            #     executor.submit(self.switch_meetings, executedDriver)
            with concurrent.futures.ThreadPoolExecutor() as executor:
                keep_alive_future = [executor.submit(self.switch_meetings, *future.result()) for future in concurrent.futures.as_completed(futures)]
                concurrent.futures.wait(keep_alive_future)
                time.sleep(10)


    def cleanup(self):
        logging.info("Browser windows cleaned up and closing the program using soft termination.\n\n\n")
        for driver in self.drivers:
            driver.quit()

    def terminate_simulation(self):
        self.terminate_automation = True


# Set the URL of the meeting
meeting_url = input('Enter the link: ')
maximum_tabs = 8
# Set the number of guest users to simulate
num_users = 24

# Set the path to the Chrome webdriver
webdriver_path = r"C:\Users\Saurabh16.Yadav\Desktop\jiomeet\chromedriver.exe"

# Create an instance of MeetingSimulator and simulate the meeting

if __name__ == '__main__':
    simulator = MeetingSimulator(meeting_url, num_users, webdriver_path)
    try:
        simulator.simulate()
    except Exception as e:
        logging.error(f"An error occurred during the simulation: {str(e)} \n\n\n", exc_info=True)
    finally:
        simulator.cleanup()
