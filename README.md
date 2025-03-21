# Selenium Login Bot

This project is a Selenium-based web automation script that automates logging into a website using a username and password. The script is designed to work with Google Chrome and requires `chromedriver` to be installed.

## Features
- Automates login to websites using Selenium WebDriver.
- Uses environment variables for credentials security.
- Handles incorrect paths and invalid URLs gracefully.
- Implements implicit waits for better element interaction.

## Prerequisites
- Python 3.x installed
- Google Chrome installed
- ChromeDriver installed (Ensure the path is correctly set in the script)
- Selenium package installed (`pip install selenium`)

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo/selenium-login-bot.git
   cd selenium-login-bot
   ```
2. Install dependencies:
   ```sh
   pip install selenium
   ```
3. Download and set up ChromeDriver:
   - Ensure `chromedriver.exe` is installed in the specified path (`CHROMEDRIVER_PATH`).

## Usage
1. Set up environment variables (Optional):
   ```sh
   export USERNAME='your_username'
   export PASSWORD='your_password'
   ```
   Or modify the script directly.

2. Run the script:
   ```sh
   python script.py
   ```

3. Enter the website URL when prompted:
   ```
   Enter the URL (e.g., www.linkedin.com):
   ```
   The script will automatically add "https://" if missing.

## Notes
- Ensure the correct ChromeDriver version is installed for your Chrome browser.
- The script uses `implicitly_wait(10)` for smoother execution.
- Update selectors (`By.NAME`, `By.CSS_SELECTOR`) if website elements change.

## License
This project is open-source and available for modification and distribution.

## Author
Alina Afzal

