from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

# Set up the Chrome WebDriver
service = Service(r'C:\Users\Chira\OneDrive\Desktop\hcaptcha-solver-python-selenium-master\chromedriver-win64\chromedriver.exe')
driver = webdriver.Chrome(service=service)

# Track test case results
test_results = {
    "Open the home page": False,
    "Navigate to the signup page": False,
    "Click on Login link": False,
    "Enter login details": False,
    "Navigate to agroproducts page": False,
    "Scroll down and interact with the first product": False,
    "Scroll down to show the purchased product": False,
    "Click on Logout": False
}

def report_result(test_case, success, message=''):
    if success:
        print(f"{test_case}: Passed")
    else:
        print(f"{test_case}: Failed - {message}")
    test_results[test_case] = success

try:
    # Maximize the browser window
    driver.maximize_window()

    # Test Case 1: Open the home page
    try:
        print("Test Case 1: Open the home page")
        driver.get("http://127.0.0.1:5000/")
        time.sleep(4)  # Wait for 4 seconds
        report_result("Open the home page", True)
    except Exception:
        report_result("Open the home page", False, "Unable to open the home page.")

    # Test Case 2: Navigate to the signup page
    try:
        print("Test Case 2: Navigate to the signup page")
        driver.get("http://127.0.0.1:5000/signup")
        time.sleep(2)  # Wait for the signup page to load
        report_result("Navigate to the signup page", True)
    except Exception:
        report_result("Navigate to the signup page", False, "Unable to navigate to the signup page.")

    # Test Case 3: Click on "Login" link on the signup page
    try:
        print("Test Case 3: Click on 'Login' link on the signup page")
        login_link = driver.find_element(By.LINK_TEXT, 'Login')
        login_link.click()
        time.sleep(3)  # Wait for the login form to appear
        report_result("Click on Login link", True)
    except Exception:
        report_result("Click on Login link", False, "Login link not found or click failed.")

    # Test Case 4: Enter login details
    try:
        print("Test Case 4: Enter login details")
        email_input = driver.find_element(By.NAME, 'email')
        password_input = driver.find_element(By.NAME, 'password')
        email_input.send_keys('vemana9@gmail.com')
        password_input.send_keys('test')
        password_input.send_keys(Keys.RETURN)
        time.sleep(4)  # Wait for login to complete
        report_result("Enter login details", True)
    except Exception:
        report_result("Enter login details", False, "Login failed. Unable to find input fields or submit login.")

    # Test Case 5: Navigate to agroproducts page
    try:
        print("Test Case 5: Navigate to agroproducts page")
        driver.get("http://127.0.0.1:5000/agroproducts")
        time.sleep(4)  # Wait for the agroproducts page to load
        report_result("Navigate to agroproducts page", True)
    except Exception:
        report_result("Navigate to agroproducts page", False, "Unable to navigate to agroproducts page.")

    # Test Case 6: Scroll down and interact with the first product
    try:
        print("Test Case 6: Scroll down and interact with the first product")
        driver.execute_script("window.scrollBy(0, 500);")
        time.sleep(2)
        quantity_input = driver.find_element(By.XPATH, "//input[@name='quantity']")
        quantity_input.clear()
        quantity_input.send_keys("60")
        time.sleep(3)  # Wait for 3 seconds
        purchase_button = driver.find_element(By.XPATH, "//button[text()='Purchase']")
        purchase_button.click()
        time.sleep(5)  # Wait for the purchase to process
        report_result("Scroll down and interact with the first product", True)
    except Exception:
        report_result("Scroll down and interact with the first product", False, "Unable to interact with the first product.")

    # Test Case 7: Scroll down to show the purchased product
    try:
        print("Test Case 7: Scroll down to show the purchased product")
        driver.execute_script("window.scrollBy(0, 500);")
        time.sleep(2)
        report_result("Scroll down to show the purchased product", True)
    except Exception:
        report_result("Scroll down to show the purchased product", False, "Unable to scroll down to show the purchased product.")

    # Test Case 8: Click on Logout
    try:
        print("Test Case 8: Click on Logout")
        logout_button = driver.find_element(By.XPATH, "//a[@href='/logout']")
        driver.execute_script("arguments[0].scrollIntoView(true);", logout_button)
        time.sleep(2)
        logout_button.click()
        time.sleep(5)  # Wait for logout to complete
        report_result("Click on Logout", True)
    except Exception:
        report_result("Click on Logout", False, "Logout button not found or click failed.")

finally:
    # Close the browser
    driver.quit()

# Summary
all_passed = all(test_results.values())
if all_passed:
    print("All test cases executed successfully.")
else:
    print("Test cases executed but some failed.")
