import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Initialize ChromeDriver service
service = Service("C:/driver/chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("http://10.10.99.39:8002/login")

actual_title = driver.title
expected_title = "DOST PPM"
if expected_title not in actual_title:
    raise AssertionError("Login Test Failed")
else:
    print("Login Successfully")
# Open login page


# Wait for elements
wait = WebDriverWait(driver, 10)
username = wait.until(EC.presence_of_element_located((By.NAME, "email")))
password = wait.until(EC.presence_of_element_located((By.NAME, "password")))
login_button = wait.until(EC.element_to_be_clickable((By.ID, "btnLogin")))

# Enter credentials and login
username.send_keys("marllesterflorida@gmail.com")
password.send_keys("Dost@1234")
login_button.click()

# Wait for page to load
time.sleep(5)

# Validate page title


try:
    input("Press Enter to close the browser...")
finally:
    driver.quit()
# Close browser
#driver.quit()
