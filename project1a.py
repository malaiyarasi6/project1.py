from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize WebDriver
driver = webdriver.Chrome()

# Test Data
url = "https://<company_orangehrm_url>/auth/login"  # Replace with actual OrangeHRM URL
username = "admin"  # Replace with valid username
password = "admin_password"  # Replace with valid password
first_name = "John"
middle_name = "A"
last_name = "Doe"
employee_id = "12345"  # Optional, can be left blank for auto-generated ID

# New details for editing
updated_first_name = "Jonathan"
updated_middle_name = "B"
updated_last_name = "Smith"

# Step 1: Open the login page
driver.get(url)

try:
    # Step 2: Log into OrangeHRM
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "txtUsername"))).send_keys(username)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "txtPassword"))).send_keys(password)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "btnLogin"))).click()

    # Step 3: Navigate to PIM Module
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "menu_pim_viewPimModule"))).click()

    # Step 4: Click on Add Employee
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "menu_pim_addEmployee"))).click()

    # Step 5: Fill in new employee details
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "firstName"))).send_keys(first_name)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "middleName"))).send_keys(middle_name)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "lastName"))).send_keys(last_name)
    
    # Optional: Fill in Employee ID if provided
    emp_id_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "employeeId")))
    emp_id_field.clear()
    emp_id_field.send_keys(employee_id)

    # Step 6: Save the new employee details
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "btnSave"))).click()

    # Verify the Personal Details page is displayed as a confirmation
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Personal Details')]")))
    print("Test Passed: New employee was successfully added.")

    # Step 7: Search for the new employee in the PIM list
    # Navigate back to the employee list
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "menu_pim_viewEmployeeList"))).click()

    # Search by employee ID
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "empsearch_id"))).send_keys(employee_id)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "searchBtn"))).click()

    # Click on the employee name link to edit details
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, first_name + " " + last_name))).click()

    # Step 8: Edit employee details
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "btnSave"))).click()  # Click Edit button

    # Update first name, middle name, and last name
    first_name_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "personal_txtEmpFirstName")))
    first_name_field.clear()
    first_name_field.send_keys(updated_first_name)

    middle_name_field = driver.find_element(By.ID, "personal_txtEmpMiddleName")
    middle_name_field.clear()
    middle_name_field.send_keys(updated_middle_name)

    last_name_field = driver.find_element(By.ID, "personal_txtEmpLastName")
    last_name_field.clear()
    last_name_field.send_keys(updated_last_name)

    # Save updated details
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "btnSave"))).click()

    # Verify the updated name is saved
    updated_name = driver.find_element(By.ID, "personal_txtEmpFirstName").get_attribute("value")
    if updated_name == updated_first_name:
        print("Test Passed: Employee information was successfully updated.")
    else:
        print("Test Failed: Employee information was not updated as expected.")

    # Step 9: Delete the employee
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "menu_pim_viewEmployeeList"))).click()
    
    # Search for the employee to delete
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "empsearch_id"))).send_keys(employee_id)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "searchBtn"))).click()

    # Select the checkbox next to the employee and delete
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "chkSelectRow[]"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "btnDelete"))).click()

    # Confirm deletion in the popup dialog
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "dialogDeleteBtn"))).click()

    print("Test Passed: Employee was successfully deleted.")

except Exception as e:
    print(f"Test Failed: An exception occurred - {e}")

finally:
    # Close the browser
    time.sleep(2)
    driver.quit()


