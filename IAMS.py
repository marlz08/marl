import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Initialize ChromeDriver service
service = Service("C:/driver/chromedriver.exe")
driver = webdriver.Chrome(service=service)

try:
    driver.get("http://10.10.99.18:8002/auditor")
    wait = WebDriverWait(driver, 10)

    # --- Username Field ---
    username = wait.until(EC.presence_of_element_located((By.NAME, "username")))
    username.clear()
    username.send_keys("marllesterflorida@gmail.com")
    print("Username entered.")
    time.sleep(1)

    # Assert that the username matches the expected value
    assert username.get_attribute(
        "value") == "marllesterflorida@gmail.com", "Username does not match the expected value!"

    # --- Password Field ---
    password = wait.until(EC.presence_of_element_located((By.NAME, "password")))
    password.clear()
    password.send_keys("Dost@1234")
    print("Password entered.")
    time.sleep(1)

    # Assert that the password matches the expected value
    assert password.get_attribute("value") == "Dost@1234", "Password does not match the expected value!"

    # --- Login Button ---
    login_button = wait.until(EC.element_to_be_clickable((By.ID, "login")))
    login_button.click()
    print("Login button clicked.")
    time.sleep(1)

    # --- Wait for ICQ Page ---
    wait.until(EC.title_contains("ICQ"))
    print("Login Successful: ICQ page loaded.")
    time.sleep(1)

    # --- Date Field ---
    date_of_audit = wait.until(EC.element_to_be_clickable((By.ID, "icq_date")))
    date_of_audit.clear()
    date_of_audit.send_keys("04/24/2025")
    print("Date entered.")
    time.sleep(1)

    # --- Auditees ---
    auditees = wait.until(EC.element_to_be_clickable((By.ID, "icq_auditees")))
    auditees.clear()
    auditees.send_keys("marl")
    print("Auditees entered.")
    time.sleep(1)

    # --- Wait for Table Body ---
    tbody = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="tbl-icq-findings-body"]')))
    print("Table body located.")
    time.sleep(1)

    # --- Click on 'Category 1' Row ---
    category_1_td = wait.until(EC.element_to_be_clickable((
        By.XPATH,
        '//td[@class="updateIcqParticularsRow" and normalize-space(.//strong)="Category 1"]'
    )))
    driver.execute_script("arguments[0].scrollIntoView(true);", category_1_td)
    time.sleep(1)
    category_1_td.click()
    print("Clicked on 'Category 1' successfully.")
    time.sleep(1)

    # --- Input Comment in Textarea ---
    comment_box = wait.until(EC.presence_of_element_located((
        By.XPATH,
        '//textarea[@class="form-control"]'
    )))
    driver.execute_script("arguments[0].scrollIntoView(true);", comment_box)
    comment_box.clear()
    comment_box.send_keys("Hi, how are you?")
    print("Comment entered successfully.")
    time.sleep(1)

    # --- Wait for  Modal to be Visible ---
    cat1 = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="icqModal"]')))
    print("Modal is visible.")
    time.sleep(1)

    # --- Wait for Close Button and Click It ---
    close_button = wait.until(EC.element_to_be_clickable((
        By.XPATH, '//*[@id="icqModal"]/div/div/div[1]/button'
    )))
    print("Close button found.")

    # Scroll to the button before clicking it
    driver.execute_script("arguments[0].scrollIntoView(true);", close_button)
    time.sleep(1)

    # Click the close button
    driver.execute_script("arguments[0].click();", close_button)
    print(" Modal closed .")
    time.sleep(1)

    # --- Click on 'Category 2' Row ---
    category_2_td = wait.until(EC.element_to_be_clickable((
        By.XPATH,
        '//td[@class="updateIcqParticularsRow" and normalize-space(.//strong)="Category 2"]'
    )))
    driver.execute_script("arguments[0].scrollIntoView(true);", category_2_td)
    time.sleep(1)
    category_2_td.click()
    print("Clicked on 'Category 2' successfully.")
    time.sleep(1)

    # --- Wait for Modal to be Visible ---
    cat2 = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="icqModal"]')))
    print("Modal is visible.")
    time.sleep(1)

    # --- Wait for Close Button and Click It ---
    close_button = wait.until(EC.element_to_be_clickable((
        By.XPATH, '//*[@id="icqModal"]/div/div/div[1]/button'
    )))
    print("Close button found.")

    # Scroll to the button before clicking it
    driver.execute_script("arguments[0].scrollIntoView(true);", close_button)
    time.sleep(1)

    # Click the close button
    driver.execute_script("arguments[0].click();", close_button)
    print(" Modal closed .")
    time.sleep(1)

    # --- Click on 'Sample 1' Row ---
    Sample_1_td = wait.until(EC.element_to_be_clickable((
        By.XPATH,
        '//td[@class="updateIcqParticularsRow" and normalize-space(.//strong)="Sample 1"]'
    )))
    driver.execute_script("arguments[0].scrollIntoView(true);", Sample_1_td)
    time.sleep(1)
    Sample_1_td.click()
    print("Clicked on 'Sample 1' successfully.")
    time.sleep(1)

    # --- Wait for Modal to be Visible ---
    sam1 = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="icqModal"]')))
    print("Modal is visible.")
    time.sleep(1)

    # --- Wait for Close Button and Click It ---
    close_button = wait.until(EC.element_to_be_clickable((
        By.XPATH, '//*[@id="icqModal"]/div/div/div[1]/button'
    )))
    print("Close button found.")

    # Scroll to the button before clicking it
    driver.execute_script("arguments[0].scrollIntoView(true);", close_button)
    time.sleep(1)

    # Click the close button
    driver.execute_script("arguments[0].click();", close_button)
    print(" Modal closed .")
    time.sleep(1)

    # --- Click on 'Sample 2' Row ---
    Sample_2_td = wait.until(EC.element_to_be_clickable((
        By.XPATH,
        '//td[@class="updateIcqParticularsRow" and normalize-space(.//strong)="Sample 2"]'
    )))
    driver.execute_script("arguments[0].scrollIntoView(true);", Sample_2_td)
    time.sleep(1)
    Sample_2_td.click()
    print("Clicked on 'Sample 2' successfully.")
    time.sleep(1)

    # --- Wait for Modal to be Visible ---
    sam2 = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="icqModal"]')))
    print("Modal is visible.")
    time.sleep(1)

    # --- Wait for Close Button and Click It ---
    close_button = wait.until(EC.element_to_be_clickable((
        By.XPATH, '//*[@id="icqModal"]/div/div/div[1]/button'
    )))
    print("Close button found.")

    # Scroll to the button before clicking it
    driver.execute_script("arguments[0].scrollIntoView(true);", close_button)
    time.sleep(1)

    # Click the close button
    driver.execute_script("arguments[0].click();", close_button)
    print(" Modal closed .")
    time.sleep(1)

    # --- Click on 'Risk Managemen' Row ---
    Risk_Managemen_td = wait.until(EC.element_to_be_clickable((
        By.XPATH,
        '//td[@class="updateIcqParticularsRow" and normalize-space(.//strong)="Risk Managemen"]'
    )))
    driver.execute_script("arguments[0].scrollIntoView(true);", Risk_Managemen_td)
    time.sleep(1)
    Risk_Managemen_td.click()
    print("Clicked on 'Risk Managemen' successfully.")
    time.sleep(1)

    # --- Wait for Modal to be Visible ---
    Risk = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="icqModal"]')))
    print("Modal is visible.")
    time.sleep(1)

    # --- Wait for Close Button and Click It ---
    close_button = wait.until(EC.element_to_be_clickable((
        By.XPATH, '//*[@id="icqModal"]/div/div/div[1]/button'
    )))
    print("Close button found.")

    # Scroll to the button before clicking it
    driver.execute_script("arguments[0].scrollIntoView(true);", close_button)
    time.sleep(1)

    # Click the close button
    driver.execute_script("arguments[0].click();", close_button)
    print(" Modal closed .")
    time.sleep(1)

    # --- RM_Q4 ---
    RM_Q4_td = wait.until(EC.element_to_be_clickable((
        By.XPATH,
        '//*[@id="tbl-icq-findings-body"]/tr[9]/td[2]/span'
    )))
    driver.execute_script("arguments[0].scrollIntoView(true);", RM_Q4_td)
    RM_Q4_td.click()
    print("Clicked on 'RM_Q4'.")
    time.sleep(1)

    # --- Yes ---
    Yes_td = wait.until(EC.element_to_be_clickable((
        By.XPATH,
        '//*[@id="fndYes"]'
    )))
    driver.execute_script("arguments[0].scrollIntoView(true);", Yes_td)
    Yes_td.click()
    print("Clicked on 'Yes'.")
    time.sleep(1)

    # --- No ---
    No_td = wait.until(EC.element_to_be_clickable((
        By.XPATH,
        '//*[@id="fndNo"]'
    )))
    driver.execute_script("arguments[0].scrollIntoView(true);", No_td)
    No_td.click()
    print("Clicked on 'No'.")
    time.sleep(1)

    # --- Na ---
    Na_td = wait.until(EC.element_to_be_clickable((
        By.XPATH,
        '//*[@id="fndNa"]'
    )))
    driver.execute_script("arguments[0].scrollIntoView(true);", Na_td)
    Na_td.click()
    print("Clicked on 'Na'.")
    time.sleep(1)

    # --- File ---
    File_td = wait.until(EC.element_to_be_clickable((
        By.XPATH,
        '//*[@id="fndRemarks"]/div[2]/div[1]/div[1]/div[2]/button[1]'
    )))
    driver.execute_script("arguments[0].scrollIntoView(true);", File_td)
    File_td.click()
    print("Clicked on 'File'.")
    time.sleep(1)

    # --- Edit ---
    Edit_td = wait.until(EC.element_to_be_clickable((
        By.XPATH,
        '//*[@id="fndRemarks"]/div[2]/div[1]/div[1]/div[2]/button[2]'
    )))
    driver.execute_script("arguments[0].scrollIntoView(true);", Edit_td)
    Edit_td.click()
    print("Clicked on 'Edit'.")
    time.sleep(1)


except TimeoutException as te:
    print(f"Timeout error: {te}")
    driver.quit()  # Exit if there's a timeout
except AssertionError as ae:
    print(f"Assertion Error: {ae}")
    driver.quit()  # Exit if credentials do not match the expected values
except Exception as e:
    print(f"Unexpected error: {e}")
    driver.quit()  # Exit for any other unexpected errors
finally:
    input("Press Enter to close the browser manually...")
    driver.quit()
