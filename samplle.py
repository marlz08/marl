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
    if not (username.is_displayed() and username.is_enabled()):
        raise Exception("Username field not interactable")
    username.clear()
    username.send_keys("marllesterflorida@gmail.com")
    if username.get_attribute("value") != "marllesterflorida@gmail.com":
        raise Exception("Username not correctly entered")

    # --- Password Field ---
    password = wait.until(EC.presence_of_element_located((By.NAME, "password")))
    if not (password.is_displayed() and password.is_enabled()):
        raise Exception("Password field not interactable")
    password.clear()
    password.send_keys("Dost@1234")

    # --- Login Button ---
    login_button = wait.until(EC.element_to_be_clickable((By.ID, "login")))
    if not login_button.is_displayed():
        raise Exception("Login button not visible")
    login_button.click()

    # --- Login Validation ---
    wait.until(EC.title_contains("ICQ"))
    print("Login Successful: ICQ page loaded.")

    # --- Date Field ---
    date_of_audit = wait.until(EC.element_to_be_clickable((By.ID, "icq_date")))
    date_of_audit.clear()
    date_of_audit.send_keys("04/24/2025")

    # --- Auditees ---
    auditees = wait.until(EC.element_to_be_clickable((By.ID, "icq_auditees")))
    auditees.clear()
    auditees.send_keys("marl")

    # --- Table Extraction ---
    #tbody = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="tbl-icq-findings-body"]')))
    #data = []

    #for tr in tbody.find_elements(By.XPATH, './/tr'):
      #  cells = tr.find_elements(By.XPATH, './/td')
     #   row = [cell.text.strip() for cell in cells]
    #    data.append(row)

   # print("\nExtracted Table Data:")
   # for row in data:
       # print(row)

##############





except TimeoutException as te:
    print(f"Timeout error: {te}")
except Exception as e:
    print(f"Unexpected error: {e}")
finally:
    input("Press Enter to close the browser manually...")
    driver.quit()
