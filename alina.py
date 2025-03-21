# Used to import the webdriver from selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os
import time

# Get the path of chromedriver which you have installed
def startBot(username, password, url):
    path = os.getenv("CHROMEDRIVER_PATH", r"C:\Users\hp\Downloads\chromedriver-win64 (1)\chromedriver-win64\chromedriver.exe")
    
    # Check if the path exists
    if not os.path.exists(path):
        raise FileNotFoundError("Chromedriver not found at the specified path.")
    
    # Validate the URL
    if not url.startswith("http://") and not url.startswith("https://"):
        raise ValueError("The provided URL is not valid. Please ensure it starts with 'http://' or 'https://'.")
    
    print(f"Navigating to URL: {url}")  # Log the URL being accessed
    
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Create a Service object
    service = Service(path)
    
    # giving the path of chromedriver to selenium webdriver
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    # opening the website in chrome.
    driver.get(url)
    
    try:
        # find the username input
        driver.implicitly_wait(10)  # Wait for elements to be present
        driver.find_element(By.NAME, "session_key").send_keys(username)  # Updated selector



        
        # find the password input
        driver.find_element(By.NAME, "session_password").send_keys(password)  # Updated selector



        
        # click on submit
        driver.find_element(By.CSS_SELECTOR, ".btn__primary--large").click()  # Updated selector



    except Exception as e:
        print(f"An error occurred: {e}")
        time.sleep(60)  # Keep the browser open for 60 seconds
    finally:
        driver.quit()


# Driver Code
# Enter below your login credentials
username = os.getenv("USERNAME", "ALINA")
password = os.getenv("PASSWORD", "1234")

# Prompt for the URL of the login page of the site
url = input("Enter the URL (e.g., www.linkedin.com): ")
if not url.startswith("http://") and not url.startswith("https://"):
    url = "https://" + url

# Call the function
startBot(username, password, url)  

 