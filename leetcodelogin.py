from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Function to read credentials from a file
def get_credentials_from_file(filename):
    with open(filename, 'r') as file:
        # Read lines and remove leading/trailing whitespaces
        lines = [line.strip() for line in file.readlines()]
        return lines[0], lines[1] if len(lines) > 1 else ''

# Set the path to geckodriver
#geckodriver_path = '/home/kali/Downloads/geckodriver'

# Create a Firefox Service object
#firefox_service = Service(geckodriver_path)
firefox_service = Service()

# Create Firefox WebDriver instance
firefox_options = webdriver.FirefoxOptions()

# Uncomment the next line if you want to run in headless mode
firefox_options.add_argument('--headless')

# Set the binary location for Firefox (modify as needed)
firefox_options.binary_location = "/usr/bin/firefox"

# Set the Service object in the Firefox options
firefox_options.service = firefox_service

# Create the Firefox WebDriver instance
firefox_driver = webdriver.Firefox(options=firefox_options)

# Open the LeetCode login page
leetcode_login_url = 'https://leetcode.com/accounts/login/?next=/points/'
firefox_driver.get(leetcode_login_url)

# Print the current URL (you can add further actions or verifications here)
print("Navigated to:", firefox_driver.current_url)

# Read username and password from file
credentials_filename = '/home/kali/Downloads/your_credentials.txt'
username, password = get_credentials_from_file(credentials_filename)

# Find the input fields using their IDs and send keys
username_field = firefox_driver.find_element('id', 'id_login')
password_field = firefox_driver.find_element('id', 'id_password')

username_field.send_keys(username)
password_field.send_keys(password)

# Find and click the "Sign In" button
signin_button = WebDriverWait(firefox_driver, 10).until(
    EC.element_to_be_clickable((By.ID, 'signin_btn'))
)
signin_button.click()

# Allow time for the page to load (you may need to adjust this)
time.sleep(10)

# Print the current URL (you can add further actions or verifications here)
print("Navigated to:", firefox_driver.current_url)

# Retrieve data from the specified path
data_element = WebDriverWait(firefox_driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '#points-app > div > div > div.col-md-8.col-md-push-2 > div.points-container > ul > span > li:nth-child(1) > div'))
)

# Get and print the data
data = data_element.text
print("Data from the specified path:", data)

# Navigate to https://leetcode.com/ramu_garkini/
firefox_driver.get("https://leetcode.com/ramu_garkini/")

# Allow time for the page to load (you may need to adjust this)
time.sleep(10)

# Print the current URL (you can add further actions or verifications here)
print("Navigated to:", firefox_driver.current_url)

# Navigate to
firefox_driver.get("https://leetcode.com/points/")

# Allow time for the page to load (you may need to adjust this)
time.sleep(10)

# Print the current URL (you can add further actions or verifications here)
print("Navigated to:", firefox_driver.current_url)

# Retrieve data from the specified path
data_element = WebDriverWait(firefox_driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '#points-app > div > div > div.col-md-8.col-md-push-2 > div.points-container > ul > span > li:nth-child(1) > div'))
)

# Get and print the data
data = data_element.text
print("Data from the specified path:", data)

# Navigate to https://leetcode.com/accounts/logout/
firefox_driver.get("https://leetcode.com/accounts/logout/")

# Allow time for the page to load (you may need to adjust this)
time.sleep(10)

# Print the current URL (you can add further actions or verifications here)
print("Navigated to:", firefox_driver.current_url)

# Find and click the "Sign Out" button
signout_button = WebDriverWait(firefox_driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '#base_content > div > form > button'))
)
signout_button.click()

# Allow time for the page to load (you may need to adjust this)
time.sleep(10)

# Print the current URL (you can add further actions or verifications here)
print("Navigated to:", firefox_driver.current_url)

# Close the browser window
firefox_driver.quit()