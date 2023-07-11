# Meeting Stress Test

This repository contains a Python script `meeting_stress_test.py` that automates the process of simulating multiple users joining a meeting using the JioMeet video conferencing platform. This stress test can help evaluate the performance and stability of the JioMeet platform under heavy user load.

## Requirements
To run the script, make sure you have the following installed:
- Python 3.x: Python is a popular programming language widely used for automation tasks.
- Selenium library: Selenium is a powerful tool for automating web browsers. It provides a convenient API for interacting with web pages and performing various actions.
- Chrome WebDriver: WebDriver is a tool that enables automated testing of web applications. It allows Selenium to control a web browser, such as Google Chrome, for automated tasks.

## Installation

1. Clone the repository to your local machine:

```
git clone https://github.com/RoyalMamba/Jiomeet_Automate.git
```

2. Navigate to the project directory:

```
cd Jiomeet_Automate
```

3. Install the required dependencies:

```
pip install -r requirements.txt
```

4. Download the Chrome WebDriver and place it in the project directory. The Chrome WebDriver is required to control the Google Chrome browser. You can download the Chrome WebDriver from the [official website](https://sites.google.com/a/chromium.org/chromedriver/downloads). Make sure to choose the version that matches your Chrome browser version.

## Usage

1. Open the `meeting_stress_test.py` file in a text editor.

2. Set the following variables at the top of the script:

- `meeting_url`: Enter the URL of the JioMeet meeting you want to simulate. This should be a valid JioMeet meeting link.
- `maximum_tabs`: Set the maximum number of tabs to open in each browser window. This determines the number of parallel users that can join the meeting. Adjust this value based on your system's capabilities and the desired stress level for the meeting.
- `num_users`: Set the total number of users to simulate joining the meeting. This determines the overall load on the JioMeet platform during the stress test.
- `webdriver_path`: Set the path to the Chrome WebDriver executable. This should be the path to the downloaded Chrome WebDriver file on your system.

3. Save the changes to the file.

4. Open a terminal or command prompt and navigate to the project directory.

5. Run the script using the following command:

```
python meeting_stress_test.py
```

6. The script will open multiple browser windows with tabs and simulate users joining the meeting. Each user will be named as "Guest User 1", "Guest User 2", and so on, with a unique number assigned to them. The script will automatically fill in the name field and click the join button for each user. The meeting tabs will be distributed across the browser windows based on the maximum number of tabs set.

7. The script will also periodically switch between the meeting tabs in each browser window. This is done to simulate users actively participating in the meeting by interacting with different tabs.

8. To stop the simulation and terminate the program, press the `Esc` key at any time.

## Contributing

If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request. Your contributions are welcome!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
