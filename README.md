# LeetCode Automation Script

This project is a Python script designed to automate interactions with the LeetCode platform. The script logs into a user account, retrieves specific data (such as points), and logs out. It uses **Selenium** for web automation and works with the **Firefox** browser.

## Why This Project?
This script is designed for automating the process of collecting **daily rewards** on LeetCode. It logs into your account, retrieves points or other relevant data for the day, and logs out, all without requiring manual intervention. This is ideal for users who want to automate their daily activities on the platform to consistently earn rewards without having to manually log in every day.

## Features

### 1. Automated Web Login
- Logs into the LeetCode platform using credentials stored in an external file.
- Supports headless browsing (no graphical interface) for background operation.

### 2. Data Retrieval
- Retrieves specific data (e.g., user points) from a designated page after logging in.
- Data is extracted from the page dynamically after it has loaded.

### 3. Multi-page Navigation
- Automatically navigates between multiple pages (e.g., profile, points page).
- Allows for extraction of data from different parts of the platform.

### 4. Logout Automation
- Logs out from the LeetCode account after completing the required actions.

### 5. Time Delays and Synchronization
- Includes time delays (`time.sleep()`) to ensure proper loading of pages.
- Uses `WebDriverWait` for more reliable synchronization of page elements.

### 6. Reading Credentials from a File
- Credentials are read from an external file, making the script easy to modify and automate with different accounts.


## Setup

### Prerequisites
- Python 3.x
- Selenium package
- Firefox browser and the corresponding **Geckodriver** installed.

### Installation
1. Install Selenium:
    ```bash
    pip install selenium
    ```

2. Download the correct **Geckodriver** version for your platform:  
   [Geckodriver Downloads](https://github.com/mozilla/geckodriver/releases)

3. Place your **credentials file** (`your_credentials.txt`) in the appropriate directory with the following format:

4. Run the script with the following command:
 ```bash
 python leetcodelogin.py
 ```

