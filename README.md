## Meeting Stress Testing Script

This script utilizes Selenium WebDriver to simulate joining a meeting with multiple guest users for stress testing purposes. It opens multiple Chrome browser windows and joins the specified meeting URL with each user.

### Prerequisites

- Python 3.x
- Selenium library (`pip install selenium`)
- Chrome WebDriver (compatible with your installed version of Chrome)

### Setup

1. Clone or download this repository to your local machine.

2. Install the required dependencies by running the following command:

   ```bash
   pip install selenium
   ```

3. Download the appropriate Chrome WebDriver from the official website (https://sites.google.com/a/chromium.org/chromedriver/downloads) and place it in a directory of your choice.

4. Open the script file `meeting_stress_test.py` in a text editor and modify the following variables:

   - `meeting_url`: Set the URL of the meeting you want to stress test.
   - `num_users`: Set the number of guest users to simulate.
   - `webdriver_path`: Set the path to the Chrome WebDriver executable.

### Usage

1. Open a command prompt or terminal.

2. Navigate to the directory containing the script and dependencies.

3. Run the script using the following command:

   ```bash
   python meeting_stress_test.py
   ```

4. The script will open multiple Chrome browser windows and join the meeting URL with each guest user. The users will be named as "Guest User 1", "Guest User 2", and so on.

5. Monitor the script execution and any error messages that may occur.

### Customization

- You can modify the code to work with a different browser by changing the WebDriver and options accordingly.

- If desired, you can uncomment the line `options.add_argument("--headless")` in the script to run it in headless mode without opening a visible browser window.

### License

This script is provided under the [MIT License](LICENSE).

Feel free to customize and adapt the code as per your requirements.

For any issues or questions, please open an [issue](https://github.com/RoyalMamba/Jiomeet_Automate/issues) on the GitHub repository.

Happy stress testing!
