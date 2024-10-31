from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize WebDriver
driver = webdriver.Chrome()

# Open the OrangeHRM login page
driver.get("https://<company_orangehrm_url>/auth/login")  # Replace with actual URL

# Test Data
valid_username = "admin"
valid_password = "correct_password"  # Replace with the actual valid password
invalid_password = "admin 123"
expected_error_message = "Invalid credentials"

def test_login(username, password, expected_message=None):
    try:
        # Locate and enter username
        username_field = driver.find_element(By.ID, "txtUsername")
        username_field.clear()
        username_field.send_keys(username)
        
        # Locate and enter password
        password_field = driver.find_element(By.ID, "txtPassword")
        password_field.clear()
        password_field.send_keys(password)
        
        # Click login button
        login_button = driver.find_element(By.ID, "btnLogin")
        login_button.click()
        
        # Wait for response
        time.sleep(2)
        
        # Check for error message if expecting failure
        if expected_message:
            error_message_element = driver.find_element(By.ID, "spanMessage")
            error_message = error_message_element.text
            if error_message == expected_message:
                print(f"Test Passed: Correct error message displayed - '{error_message}'")
            else:
                print(f"Test Failed: Expected '{expected_message}', but got '{error_message}'")
        else:
            # For valid login, verify redirection (example: check URL or dashboard element)
            if "dashboard" in driver.current_url:
                print("Test Passed: Valid login successful.")
            else:
                print("Test Failed: Login did not succeed as expected.")
    
    except Exception as e:
        print(f"Test Failed: An exception occurred - {e}")

# Run tests
print("Running Invalid Login Test...")
test_login(valid_username, invalid_password, expected_error_message)

print("\nRunning Valid Login Test...")
test_login(valid_username, valid_password)  # No expected error message for successful login

# Close the browser
driver.quit()
