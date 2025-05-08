import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import os

# Initialize ChromeDriver service
service = Service("C:/driver/chromedriver.exe")
driver = webdriver.Chrome(service=service)

try:
    driver.get("http://10.10.99.18:8002/auditor")
    wait = WebDriverWait(driver, 10)

    # Wait for the header element to appear
    login_header = wait.until(EC.presence_of_element_located((
        By.XPATH, '//*[@id="login-body"]/section/div/div/div/div/div/div[1]/div/div/h1'
    )))

    # Assertion to check the header text is "LOGIN"
    assert login_header.text.strip() == "LOGIN", f"Expected 'LOGIN', but got '{login_header.text.strip()}'"
    print("Assertion passed: LOGIN header is displayed correctly.")

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

    # --- Login Button with Assertion ---
    login_button = wait.until(EC.presence_of_element_located((By.ID, "login")))
    # Assertions
    assert login_button.is_displayed(), "Login button is not visible on the page."
    assert login_button.is_enabled(), "Login button is not enabled."
    print("Assertion passed: Login button is visible and enabled.")
    # Click the button
    login_button.click()
    print("Login button clicked.")
    time.sleep(1)

    # --- Wait and Assert ICQ Page Loaded ---
    try:
        wait.until(EC.title_contains("ICQ"))
        current_title = driver.title
        # Assert that the title contains 'ICQ'
        assert "ICQ" in current_title, f"Page title does not contain 'ICQ'. Current title: '{current_title}'"
        print("Assertion passed: Login successful, ICQ page loaded.")
    except AssertionError as ae:
        print(f"Assertion Error: {ae}")
    except Exception as e:
        print(f"Error: ICQ page did not load as expected. Exception: {e}")

    # --- Assert DOST Logo is Displayed and Loaded ---
    dost_logo = wait.until(EC.presence_of_element_located((
        By.XPATH, '//*[@id="content"]/div[1]/div/div[2]/div/div/div/div[1]/img'
    )))
    if dost_logo:
        assert dost_logo.is_displayed(), "DOST logo is not visible on the page."
        assert dost_logo.get_attribute(
            "src") == "http://10.10.99.18:8002/images/dost.png", "DOST logo source is incorrect."
        print("Assertion passed: DOST logo")
    else:
        print("DOST logo element not found on the page.")

        # --- Assert Food and Nutrition Research Institute (FNRI) Text ---
    try:
        # Wait until the element is present
        agn_name_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="agn_name"]')))
        # Extract the text
        agn_name_text = agn_name_element.text.strip()
        # Assert that the text matches the expected value
        assert agn_name_text == "Food and Nutrition Research Institute (FNRI)", f"Text mismatch! Found: {agn_name_text}"
        print("Assertion passed: Food and Nutrition Research Institute (FNRI)")
    except Exception as e:
        print(f"Assertion failed: Food and Nutrition Research Institute (FNRI) {e}")

    # --- Assert Internal Text from ara_name ---
    try:
        # Wait until the element is present
        ara_name_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="ara_name"]')))
        # Extract the text
        ara_name_text = ara_name_element.text.strip()
        # Assert that the text matches the expected value
        assert ara_name_text == "Internal", f"Text mismatch! Found: {ara_name_text}"
        print("Assertion passed: Internal")
    except Exception as e:
        print(f"Assertion failed: Internal {e}")

    # --- Assert INTERNAL CONTROL QUESTIONNAIRE (ICQ) Text ---
    try:
        # Wait until the element is present
        icq_header_element = wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div[1]/div/div[2]/div/div/div/div[1]/h5')))
        # Extract and clean the text
        icq_header_text = icq_header_element.text.strip()
        # Assert the text matches expected value
        expected_text = "INTERNAL CONTROL QUESTIONNAIRE (ICQ)"
        assert icq_header_text == expected_text, f"Text mismatch! Found: '{icq_header_text}'"
        print("Assertion passed: INTERNAL CONTROL QUESTIONNAIRE (ICQ)")
    except Exception as e:
        print(f"Assertion failed: INTERNAL CONTROL QUESTIONNAIRE (ICQ) {e}")

    # --- Date of Audit ---
    try:
        label = wait.until(EC.visibility_of_element_located((By.XPATH, '//label[@for="icq_date"]')))
        assert "Date of Audit" in label.text
        print("Assertion passed: Date of Audit")
    except Exception as e:
        print(f"Assertion failed: Date of Audit {e}")

    # --- Date input ---
    try:
        icq_date_input = wait.until(EC.presence_of_element_located((By.ID, "icq_date")))
        assert icq_date_input.is_displayed(), "ICQ date input is not visible."
        assert icq_date_input.is_enabled(), "ICQ date input is not enabled."
        print("Assertion passed: ICQ date input")
    except Exception as e:
        print(f"Assertion failed: ICQ date input {e}")

    # ---  auditees_label ---
    try:
        auditees_label = wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="auditees-container"]/div/label')))
        assert auditees_label.text.strip() == "Auditees", f"Text mismatch! Found: '{auditees_label.text.strip()}'"
        print("Assertion passed: Auditees")
    except Exception as e:
        print(f"Assertion failed: Auditees {e}")

    # ---  auditees_input ---
    try:
        auditees_input = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="icq_auditees"]')))
        # Optionally, check that the value is correct if needed
        assert auditees_input.get_attribute(
            "value") == "marl", f"Value mismatch! Found: '{auditees_input.get_attribute('value')}'"
        print("Assertion passed: Auditees input")
    except Exception as e:
        print(f"Assertion failed: Auditees input {e}")

    # --- Date Field ---
    date_of_audit = wait.until(EC.element_to_be_clickable((By.ID, "icq_date")))
    date_of_audit.clear()
    date_of_audit.send_keys("04/24/2025")
    print("Date entered")
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
    # --- Print table content ---
    print("Table content:")
    print(tbody.text)

    # --- TABLE HEADER NO ---
    try:
        # Wait for the <th> element to be present
        th_no = wait.until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="content"]/div[1]/div/div[2]/div/div/div/div[2]/div/table/thead/tr/th[1]')))
        # Get and clean the text
        th_text = th_no.text.strip()
        # Assert it matches "NO"
        assert th_text == "NO", f"Text mismatch! Expected 'NO', but found '{th_text}'"
        print("Assertion passed: Table header 'NO'")
    except Exception as e:
        print(f"Assertion failed: NO naming mismatch {e}")

    # --- TABLE HEADER PARTICULAR ---
    try:
        # Wait for the <th> element to be present
        th_particular = wait.until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="content"]/div[1]/div/div[2]/div/div/div/div[2]/div/table/thead/tr/th[2]')))
        # Get and clean the text
        th_text = th_particular.text.strip()
        # Assert it matches "PARTICULAR"
        assert th_text == "PARTICULAR", f"Text mismatch! Expected 'PARTICULAR', but found '{th_text}'"
        print("Assertion passed: Table header 'PARTICULAR'")
    except Exception as e:
        print(f"Assertion failed: PARTICULAR naming mismatch {e}")

    # --- TABLE HEADER YES or NO ---
    try:
        # Wait for the <th> element to be present
        th_yes_no = wait.until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="content"]/div[1]/div/div[2]/div/div/div/div[2]/div/table/thead/tr/th[3]')))
        # Get and clean the text
        th_text = th_yes_no.text.strip()
        # Assert the text matches
        assert th_text == "YES or NO", f"Text mismatch! Expected 'YES or NO', but found '{th_text}'"
        print("Assertion passed: Table header 'YES or NO'")
    except Exception as e:
        print(f"Assertion failed: YES or NO naming mismatch {e}")

    # --- TABLE HEADER CITE REFERENCE DOCUMENTS ---
    try:
        # Wait for the element to appear
        th_cite_ref = wait.until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="content"]/div[1]/div/div[2]/div/div/div/div[2]/div/table/thead/tr/th[4]')))
        # Get and strip the text
        th_text = th_cite_ref.text.strip()
        # Assert the expected text
        assert th_text == "CITE REFERENCE DOCUMENTS", f"Text mismatch! Expected 'CITE REFERENCE DOCUMENTS', but found '{th_text}'"
        print("Assertion passed: Table header 'CITE REFERENCE DOCUMENTS'")
    except Exception as e:
        print(f"Assertion failed: CITE REFERENCE DOCUMENTS naming mismatch {e}")

    # --- TABLE HEADER REMARKS ---
    try:
        # Wait until the 'REMARKS' header is present
        remarks_th = wait.until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="content"]/div[1]/div/div[2]/div/div/div/div[2]/div/table/thead/tr/th[5]')))
        # Get and clean the text
        remarks_text = remarks_th.text.strip()
        # Assert that the text matches the expected value
        assert remarks_text == "REMARKS", f"Text mismatch! Expected 'REMARKS', but found '{remarks_text}'"
        print("Assertion passed: Table header 'REMARKS'")
    except Exception as e:
        print(f"Assertion failed:REMARKS naming mismatch {e}")

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

    # ---Internal Control Questionnaire---
    try:
        # Wait for the modal title element to appear
        modal_title = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="icqModalLabel"]')))
        # Extract and clean the text
        modal_text = modal_title.text.strip()
        # Perform assertion
        assert modal_text == "Internal Control Questionnaire", f"Text mismatch! Expected 'Internal Control Questionnaire', but found '{modal_text}'"
        print("Assertion passed: Internal Control Questionnaire")
    except Exception as e:
        print(f"Assertion failed: Internal Control Questionnaire naming mismatch{e}")

    # ---Audit Area---
    try:
        # Wait for the Audit Area label to be present
        audit_area_label = wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="icqModalContent"]/div[1]/label')))
        # Get and clean the label text
        label_text = audit_area_label.text.strip()
        # Assert the text matches expected value
        assert label_text == "Audit Area", f"Text mismatch! Expected 'Audit Area', but found '{label_text}'"
        print("Assertion passed: Audit Area label is correct.")
    except Exception as e:
        print(f"Assertion failed: Audit Area naming mismatch{e}")

    # ---Internal---
    try:
        # Wait for the element to be present
        audit_area_value = wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="icqModalContent"]/div[1]/div')))
        # Get and clean the text
        value_text = audit_area_value.text.strip()
        # Assert it matches the expected value
        assert value_text == "Internal", f"Text mismatch! Expected 'Internal', but found '{value_text}'"
        print("Assertion passed: Audit Area value is 'Internal'.")
    except Exception as e:
        print(f"AAssertion failed: Audit Area value naming mismatch{e}")

    # --- Category ---
    try:
        # Wait for the label element
        category_label = wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="icqModalContent"]/div[2]/label')))
        # Get and clean the label text
        label_text = category_label.text.strip()
        # Assert the label matches expected text
        assert label_text == "Category", f"Text mismatch! Expected 'Category', but found '{label_text}'"
        print("Assertion passed: Category label is correct.")
    except Exception as e:
        print(f"Assertion failed: Category label naming mismatch {e}")

    # --- Category ---
    try:
        # Wait for the category value element
        category_value = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="icqModalContent"]/div[2]/div')))
        # Get and clean the text
        value_text = category_value.text.strip()
        # Assert the text matches the expected value
        assert value_text == "Category 1", f"Text mismatch! Expected 'Category 1', but found '{value_text}'"
        print("Assertion passed: Category 1")
    except Exception as e:
        print(f"Assertion failed: Category 1 {e}")

    # --- Questions ---
    try:
        # Wait for the label element
        question_label = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="icq-form"]/div[2]/label')))
        # Get and clean the text
        label_text = question_label.text.strip()
        # Assert the text matches expected
        assert label_text == "Questions", f"Text mismatch! Expected 'Questions', but found '{label_text}'"
        print("Assertion passed: 'Questions' label is correctly displayed.")
    except Exception as e:
        print(f"Assertion error: {e}")

    # --- Input Comment in Textarea ---
    comment_box = wait.until(EC.presence_of_element_located((
        By.XPATH,
        '//textarea[@class="form-control"]'
    )))
    driver.execute_script("arguments[0].scrollIntoView(true);", comment_box)
    comment_box.clear()
    comment_box.send_keys("Technology is the bridge between imagination and reality, turning dreams into everyday experiences.")
    print("Comment entered successfully.")
    time.sleep(1)

    # --- Assertion Comment in Textarea ---
    try:
        # Wait until the textarea is present
        textarea = wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="fndParticularsEntry"]/div/div[2]/textarea')))
        # Optional: Check if it's displayed and enabled
        assert textarea.is_displayed() and textarea.is_enabled(), "Textarea is not interactable."
        print("Assertion passed: Textarea is present and interactable.")
    except Exception as e:
        print(f"Assertion failed: Textarea is not working {e}")

    # --- Add Button ---
    try:
        add_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="fndParticularsEntry"]/div/div[3]/button')))
        driver.execute_script("arguments[0].scrollIntoView(true);", add_button)
        time.sleep(0.5)
        add_button.click()
        print("Add button clicked.")
    except Exception as e:
        print(f"Add button not clickable or not found: {e}")
    finally:
        print("Continuing to the next step after attempting to click the Add button.")
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
    print(" Category 1 Modal closed .")
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

    # --- Internal Control Questionnaire ---
    try:
        # Wait until the modal title is present
        modal_title = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="icqModalLabel"]')))
        # Extract and clean the text
        title_text = modal_title.text.strip()
        # Assert the expected value
        assert title_text == "Internal Control Questionnaire", f"Text mismatch! Found: '{title_text}'"
        print("Assertion passed: 'Internal Control Questionnaire' title is correct.")
    except Exception as e:
        print(f"Assertion failed: Internal Control Questionnaire naming mismatch {e}")

    # --- Audit Area ---
    try:
        audit_area_label = wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="icqModalContent"]/div[1]/label')))
        label_text = audit_area_label.text.strip()
        assert label_text == "Audit Area", f"Text mismatch! Found: '{label_text}'"
        print("Assertion passed: 'Audit Area' label is correct.")
    except Exception as e:
        print(f"Assertion failed: Audit Area label naming mismatch {e}")

    # --- Internal---
    try:
        internal_div = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="icqModalContent"]/div[1]/div')))
        internal_text = internal_div.text.strip()
        assert internal_text == "Internal", f"Text mismatch! Found: '{internal_text}'"
        print("Assertion passed: 'Internal' value is correctly displayed.")
    except Exception as e:
        print(f"Assertion failed: 'Internal' value is incorrect displayed. {e}")

    # --- Category---
    try:
        category_label = wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="icqModalContent"]/div[2]/label')))
        label_text = category_label.text.strip()
        assert label_text == "Category", f"Text mismatch! Found: '{label_text}'"
        print("Assertion passed: 'Category' label is correctly displayed.")
    except Exception as e:
        print(f"Assertion failed: 'Category' label is incorrect displayed. {e}")

    # ---Category 2---
    try:
        category_value = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="icqModalContent"]/div[2]/div')))
        value_text = category_value.text.strip()
        assert value_text == "Category 2", f"Text mismatch! Found: '{value_text}'"
        print("Assertion passed: 'Category 2' is correctly displayed.")
    except Exception as e:
        print(f"Assertion failed: 'Category 2' is incorrect displayed.{e}")

    # --- Edit the existing text in the Textarea ---
    try:
        question_label = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="icq-form"]/div[2]/label')))
        label_text = question_label.text.strip()
        assert label_text == "Questions", f"Text mismatch! Found: '{label_text}'"
        print("Assertion passed: 'Questions' label is correctly displayed.")
    except Exception as e:
        print(f"Assertion failed: 'Questions' label is incorrect displayed.{e}")

    # --- Edit the existing text in the Textarea ---
    comment_box = wait.until(EC.presence_of_element_located((
        By.XPATH,
        '//*[@id="fndParticularsEntry"]/div/div[2]/textarea'
    )))
    driver.execute_script("arguments[0].scrollIntoView(true);", comment_box)

    # Get the existing text
    existing_text = comment_box.get_attribute("value")
    print(f"Existing comment: {existing_text}")

    # Edit it (for example, add more words)
    new_text = existing_text + " In every industry, technology drives efficiency, innovation, and competitive growth."

    # Clear the box and enter new edited text
    comment_box.clear()
    comment_box.send_keys(new_text)
    print("Comment edited successfully.")
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
    print(" Category 2 Modal closed .")
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

    # --- Internal Control Questionnaire ---
    try:
        header = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="icqModalLabel"]')))
        header_text = header.text.strip()
        assert header_text == "Internal Control Questionnaire", f"Text mismatch! Found: '{header_text}'"
        print("Assertion passed: 'Internal Control Questionnaire' is correctly displayed.")
    except Exception as e:
        print(f"Assertion failed:  'Internal Control Questionnaire' is incorrect displayed {e}")

    # --- Audit Area ---
    try:
        audit_area_label = wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="icqModalContent"]/div[1]/label')))
        label_text = audit_area_label.text.strip()
        assert label_text == "Audit Area", f"Text mismatch! Found: '{label_text}'"
        print("Assertion passed: 'Audit Area' label is correctly displayed.")
    except Exception as e:
        print(f"Assertion failed: 'Audit Area' label is incorrectly displayed.{e}")

    # --- Internal ---
    try:
        audit_area_value = wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="icqModalContent"]/div[1]/div')))
        value_text = audit_area_value.text.strip()
        assert value_text == "Internal", f"Text mismatch! Expected: 'Internal', Found: '{value_text}'"
        print("Assertion passed: Audit Area value is 'Internal'.")
    except Exception as e:
        print(f"Assertion failed or element not found: {e}")

    # ---Category---
    try:
        category_label = wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="icqModalContent"]/div[2]/label')))
        label_text = category_label.text.strip()
        assert label_text == "Category", f"Text mismatch! Expected 'Category' but found '{label_text}'"
        print("Assertion passed: Category label is correct.")
    except Exception as e:
        print(f"Assertion failed:  Category label is incorrect {e}")

    # --- Sample 1---
    try:
        category_value = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="icqModalContent"]/div[2]/div')))
        value_text = category_value.text.strip()
        assert value_text == "Sample 1", f"Text mismatch! Expected 'Sample 1' but found '{value_text}'"
        print("Assertion passed: Category value is 'Sample 1'.")
    except Exception as e:
        print(f"Assertion failed: Category value is not 'Sample 1{e}")

    # ---Question ---
    try:
        label_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="icq-form"]/div[2]/label')))
        label_text = label_element.text.strip()
        assert label_text == "Questions", f"Text mismatch! Expected 'Questions' but found '{label_text}'"
        print("Assertion passed: Label text is 'Questions'.")
    except Exception as e:
        print(f"Assertion failed or element not found: {e}")

    # ---Text Area Assert ---
    try:
        # Wait until the textarea is present
        textarea = wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="fndParticularsEntry"]/div/div[2]/textarea')))
        # Check if it is displayed and enabled
        assert textarea.is_displayed(), "Textarea is not visible."
        assert textarea.is_enabled(), "Textarea is not enabled."
        print("Assertion passed: Textarea is visible and enabled.")
        # Optionally, check if it's empty
        current_text = textarea.get_attribute("value").strip()
        if current_text == "":
            print("Textarea is empty as expected.")
        else:
            print(f"Textarea is not empty. Current content: '{current_text}'")
    except Exception as e:
        print(f"Error or Assertion failed: {e}")

    # --- Add botton assertion ---
    try:
        # Wait for the button to be present
        add_button = wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="fndParticularsEntry"]/div/div[3]/button')))
        # Assertions to confirm visibility and interactivity
        assert add_button.is_displayed(), "Add button is not visible."
        assert add_button.is_enabled(), "Add button is not enabled."
        print("Assertion passed: Add button is visible and enabled.")
        # Optional: click the button to test functionality
        add_button.click()
        print("Add button clicked.")
    except Exception as e:
        print(f"Error or assertion failed: {e}")

    # --- Scroll inside existing Textarea (Up and Down) ---
    try:
        # Locate the existing textarea (no editing, just scrolling)
        comment_box = wait.until(EC.presence_of_element_located((
            By.XPATH, '//*[@id="fndParticularsEntry"]/div/div[2]/textarea'
        )))

        # Scroll to the textarea itself (to make it visible in viewport)
        driver.execute_script("arguments[0].scrollIntoView(true);", comment_box)
        time.sleep(0.5)

        # Scroll inside the textarea to the bottom
        driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;", comment_box)
        print("Scrolled to bottom of textarea.")
        time.sleep(0.5)

        # Scroll back up to the top
        driver.execute_script("arguments[0].scrollTop = 0;", comment_box)
        print("Scrolled back to top of textarea.")
        time.sleep(0.5)

    except Exception as e:
        print(f"Error scrolling inside textarea: {e}")

    # --- Wait for Modal to be Visible ---
    sam1 = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="icqModal"]')))
    print("Modal is visible.")
    time.sleep(1)

    try:
        # Wait for the button to be clickable
        close_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="icqModal"]/div/div/div[1]/button')))

        # Check if button is displayed and enabled
        assert close_button.is_displayed(), "Close button is not visible."
        assert close_button.is_enabled(), "Close button is not clickable."

        print("Assertion passed: Close button is visible and clickable.")

        # Optionally, click the button if needed
        close_button.click()
        print("Close button clicked.")
    except Exception as e:
        print(f"Error or Assertion failed: {e}")

    # Click the close button
    driver.execute_script("arguments[0].click();", close_button)
    print("Sample 1 Modal closed .")
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
    print("Sample 2 Modal closed .")
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
    print("Risk Managemen Modal closed .")
    time.sleep(1)

    # --- Click on 'Procurement Integrity' Row ---
    Procurement_td = wait.until(EC.element_to_be_clickable((
        By.XPATH,
        '//td[@class="updateIcqParticularsRow" and normalize-space(.//strong)="Procurement Integrity"]'
    )))
    driver.execute_script("arguments[0].scrollIntoView(true);", Procurement_td)
    time.sleep(1)
    Procurement_td.click()
    print("Clicked on 'Procurement Integrity' successfully.")
    time.sleep(1)

    # --- Wait for Modal to be Visible ---
    Procurement = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="icqModal"]')))
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
    print("Procurement Integrity Modal closed .")
    time.sleep(1)

    # --- Click on 'Test Only' Row ---
    Test_td = wait.until(EC.element_to_be_clickable((
        By.XPATH,
        '//td[@class="updateIcqParticularsRow" and normalize-space(.//strong)="Test only"]'
    )))
    driver.execute_script("arguments[0].scrollIntoView(true);", Test_td)
    time.sleep(1)
    Test_td.click()
    print("Clicked on 'Test Only' successfully.")
    time.sleep(1)

    # --- Wait for Modal to be Visible ---
    Test = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="icqModal"]')))
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
    print("Test Only Modal closed .")
    time.sleep(1)

    # --- Click on 'Internal Controls and Compliance' Row ---
    Internal_td = wait.until(EC.element_to_be_clickable((
        By.XPATH,
        '//td[@class="updateIcqParticularsRow" and normalize-space(.//strong)="Internal Controls and Compliance"]'
    )))
    driver.execute_script("arguments[0].scrollIntoView(true);", Internal_td)
    time.sleep(1)
    Internal_td.click()
    print("Clicked on 'Internal Controls and Compliance' successfully.")
    time.sleep(1)

    # --- Wait for and print the content that appears ---
    # Adjust the XPath below to match the panel or content area that appears after clicking
    content_container = wait.until(EC.presence_of_element_located((
        By.XPATH, '//*[@id="fndParticularsEntry"]'  # Replace with actual content container ID/XPath
    )))

    # Print the visible text inside the content container
    print("Content displayed:")
    print(content_container.text.strip())

    # --- Wait for Modal to be Visible ---
    Internal = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="icqModal"]')))
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
    print("Internal Controls and Compliance Modal closed .")
    time.sleep(1)

    # --- Q1 ---
    Q1_td = wait.until(EC.element_to_be_clickable((
        By.XPATH,
        '//*[@id="tbl-icq-findings-body"]/tr[9]/td[2]/span'
    )))
    driver.execute_script("arguments[0].scrollIntoView(true);", Q1_td)
    Q1_td.click()
    print("Clicked on 'Q1'.")
    time.sleep(1)

    # --- Internal Control Questionnaire Text assertion---
    try:
        # Wait for the modal title element to be visible
        modal_title_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="AddIcqYesNoModalLabel"]')))
        # Get the text of the modal title
        modal_title_text = modal_title_element.text.strip()
        # Assert that the title matches the expected value
        assert modal_title_text == "Internal Control Questionnaire", f"Title mismatch! Found: '{modal_title_text}'"
        print("Assertion passed: Modal title is 'Internal Control Questionnaire'.")
    except Exception as e:
        print(f"Error: {e}")

    # --- Internal Controls and Compliance Text assertion---
    try:
        # Wait for the element to be visible
        ic_category_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="icCategory"]')))
        # Get the text of the element
        ic_category_text = ic_category_element.text.strip()
        # Assert that the text matches the expected value
        assert ic_category_text == "Internal Controls and Compliance", f"Text mismatch! Found: '{ic_category_text}'"
        print("Assertion passed: Text is 'Internal Controls and Compliance'.")
    except Exception as e:
        print(f"Error: {e}")

    # ---1---
    try:
        # Wait for the element to be visible
        fnd_particular_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="fndParticular"]')))
        # Get the text of the element
        fnd_particular_text = fnd_particular_element.text.strip()
        # Assert that the text matches the expected value
        assert fnd_particular_text == "1. Were all procurement transactions supported by complete and verifiable documentation?", f"Text mismatch! Found: '{fnd_particular_text}'"
        print(
            "Assertion passed: Text is '1. Were all procurement transactions supported by complete and verifiable documentation?'")
    except Exception as e:
        print(f"Error: {e}")

    # ---Remarks / Cite Reference Documents---
    try:
        # Wait for the element to be visible
        remarks_label_element = wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="fndRemarks"]/div[1]/label')))
        # Get the text of the element
        remarks_label_text = remarks_label_element.text.strip()
        # Assert that the text matches the expected value
        assert remarks_label_text == "Remarks / Cite Reference Documents", f"Text mismatch! Found: '{remarks_label_text}'"
        print("Assertion passed: 'Remarks / Cite Reference Documents' text is correctly displayed.")
    except Exception as e:
        print(f"Error: {e}")

    # --- Yes ---
    Yes_td = wait.until(EC.element_to_be_clickable((
        By.XPATH,
        '//*[@id="fndYes"]'
    )))
    driver.execute_script("arguments[0].scrollIntoView(true);", Yes_td)
    Yes_td.click()
    print("Clicked on 'Yes'.")
    time.sleep(1)

    # --- Assertion Yes ---
    try:
        # Wait until the radio button is present
        fnd_yes_radio = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="fndYes"]')))
        # Assert that the radio button is displayed and enabled
        assert fnd_yes_radio.is_displayed(), "Radio button 'fndYes' is not visible on the page."
        assert fnd_yes_radio.is_enabled(), "Radio button 'fndYes' is not enabled."
        print("Assertion passed:  'Yes' is visible and enabled.")
        # Optionally, click the radio button if needed
        fnd_yes_radio.click()
        print("Radio button 'fndYes' clicked.")
    except Exception as e:
        print(f"EAssertion failed:  'Yes' is not visible and not enabled.{e}")

    try:
        # Wait for the label to be present
        yes_label = wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="icq-yes-no-form"]/div[1]/div[1]/label')))
        # Get and clean the text
        label_text = yes_label.text.strip()
        # Assert the label text
        assert label_text == "YES", f"Text mismatch! Found: '{label_text}'"
        print("Assertion passed: 'YES' label is correctly displayed.")
    except Exception as e:
        print(f"Error: {e}")

    # --- No ---
    No_td = wait.until(EC.element_to_be_clickable((
        By.XPATH,
        '//*[@id="fndNo"]'
    )))
    driver.execute_script("arguments[0].scrollIntoView(true);", No_td)
    No_td.click()
    print("Clicked on 'No'.")
    time.sleep(1)

    # --- No Assertion---
    try:
        # Wait for the radio button to be present
        no_radio = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="fndNo"]')))
        # Check if it is displayed and enabled
        assert no_radio.is_displayed(), "Radio button 'NO' is not visible."
        assert no_radio.is_enabled(), "Radio button 'NO' is not enabled."
        print("Assertion passed: 'NO' is visible and enabled.")
    except Exception as e:
        print(f"Error: {e}")

    try:
        # Wait until the label is present
        no_label = wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="icq-yes-no-form"]/div[1]/div[2]/label')))
        # Assert it is displayed
        assert no_label.is_displayed(), "Label 'NO' is not visible."
        print("Assertion passed: 'NO' label is visible.")
    except Exception as e:
        print(f"Error: {e}")

    ## --- Na Button ---
    try:
        Na_td = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="fndNa"]')))
        driver.execute_script("arguments[0].scrollIntoView(true);", Na_td)
        time.sleep(0.5)  # Brief wait for stability
        Na_td.click()
        print("Clicked on 'Na' button.")
    except Exception as e:
        print(f"Error clicking 'Na' button: {e}")
    finally:
        print("Proceeding to next step after 'Na'.")

    # --- Na Assertion---
        try:
            # Wait until the N/A radio button is present
            na_radio = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="fndNa"]')))
            # Assert it is displayed
            assert na_radio.is_displayed(), "Radio button 'N/A' is not visible."
            print("Assertion passed: 'N/A' is visible.")
        except Exception as e:
            print(f"Error: {e}")

        try:
            # Wait for the N.A. label to appear
            na_label = wait.until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="icq-yes-no-form"]/div[1]/div[3]/label')))
            # Check the text
            label_text = na_label.text.strip()
            assert label_text == "N.A.", f"Label mismatch! Found: '{label_text}'"
            print("Assertion passed: 'N.A.' label is correctly displayed.")
        except Exception as e:
            print(f"Error: {e}")

        # --- Assertion and Click for 'File' Button ---
        #try:
            # Wait until the "File" button is clickable
            #file_button = wait.until(
                #EC.element_to_be_clickable((By.XPATH, '//*[@id="fndRemarks"]/div[2]/div[1]/div[1]/div[2]/button[1]')))

            # Assert that the button is displayed and enabled
            #assert file_button.is_displayed(), "Button 'File' is not visible on the page."
            #assert file_button.is_enabled(), "Button 'File' is not enabled."
            #print("Assertion passed: 'File' button is visible and enabled.")

            # Click the "File" button
            #file_button.click()
            #print("Button 'File' clicked.")

        #except Exception as e:
            #print(f"Assertion failed: 'File' button is not visible or not enabled. {e}")

        # --- Enter Remarks in TinyMCE iframe ---
        remarks_iframe = wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, "fnd_remarks1_ifr")))
        remarks_body = wait.until(EC.presence_of_element_located((By.ID, "tinymce")))
        remarks_body.clear()
        remarks_body.send_keys("Hello World")
        print("Remarks entered successfully.")
        time.sleep(1)
        driver.switch_to.default_content()

    # ---  'Clear'  ---
    Clear = wait.until(EC.element_to_be_clickable((
        By.XPATH,
        '//*[@id="clearIcqYesNoRemarks"]'
    )))
    driver.execute_script("arguments[0].scrollIntoView(true);", Clear)
    time.sleep(1)
    Clear.click()
    print("Clicked on 'Clear' successfully.")
    time.sleep(1)

    # --- Upload File ---
    file_path = r"C:\Users\tess\OneDrive\Pictures\Screenshots 1\TEST.pdf"

    # --- Upload Cite Reference Document ---
    file_path = r"C:\Users\tess\OneDrive\Pictures\Screenshots 1\TEST.pdf"

    # Check if file exists
    assert os.path.exists(file_path), f"File not found at: {file_path}"

    # Scroll to the upload button (optional)
    upload_button = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="uploadCiteRefFile"]')))
    driver.execute_script("arguments[0].scrollIntoView(true);", upload_button)

    # Find the hidden file input field
    file_input = driver.find_element(By.XPATH, '//*[@id="att_cite_ref_name"]')

    # Upload the file directly (even if input is hidden)
    file_input.send_keys(file_path)
    print("Cite Reference Document uploaded successfully.")
    # --- Yes ---
    Yes_td = wait.until(EC.element_to_be_clickable((
        By.XPATH,
        '//*[@id="fndYes"]'
    )))
    driver.execute_script("arguments[0].scrollIntoView(true);", Yes_td)
    Yes_td.click()
    print("Clicked on 'Yes'.")
    time.sleep(1)

    # --- Enter Remarks in TinyMCE iframe ---
    remarks_iframe = wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, "fnd_remarks1_ifr")))
    remarks_body = wait.until(EC.presence_of_element_located((By.ID, "tinymce")))
    remarks_body.clear()
    remarks_body.send_keys("Technology continuously transforms the way we live, work, and connect, opening new possibilities with every innovation.")
    print("Remarks entered successfully.")
    driver.switch_to.default_content()

    # --- Save Button (Safe and Resilient) ---
    try:
        # Wait for the button container to be visible
        container = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="updateIcqYesNoRemarksDiv"]')))

        # Now wait for the actual button
        Save_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="updateIcqYesNoRemarks"]')))

        # Confirm the button is ready for action
        assert Save_button.is_displayed(), "Save button is not visible."
        assert Save_button.is_enabled(), "Save button is not enabled."

        print("Save button is visible and enabled. Proceeding to click.")

        # Scroll and click using ActionChains
        driver.execute_script("arguments[0].scrollIntoView(true);", Save_button)
        time.sleep(0.5)

        actions = ActionChains(driver)
        actions.move_to_element(Save_button).click().perform()

        print("Save button successfully clicked.")
        time.sleep(1)

    except AssertionError as ae:
        print(f"Assertion Error: {ae}")

    except Exception as e:
        print(f"Error: Save button not clickable or not found. Exception: {e}")

    finally:
        print("Proceeding to the next step, regardless of Save button status.")

        try:
            # Wait until the SweetAlert2 "OK" button is clickable
            ok_button = wait.until(EC.element_to_be_clickable((
                By.XPATH, '//*[@id="main-body"]/div[6]/div/div[6]/button[1]'
            )))

            # Scroll into view (optional, but useful)
            driver.execute_script("arguments[0].scrollIntoView(true);", ok_button)
            time.sleep(0.5)

            # Click the button
            ok_button.click()
            print("Completion Message OK button clicked.")

        except Exception as e:
            print(f"Failed to click the Completion Message OK button: {e}")

        ## --- Wait for Modal to be Visible ---
        #Save = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="AddIcqYesNoModal"]')))
        #print("Modal is visible.")
        #time.sleep(1)

        ## --- Wait for Close Button and Click It ---
        #close_button = wait.until(EC.element_to_be_clickable((
            #By.XPATH, '//*[@id="AddIcqYesNoModal"]/div/div/div[1]/button'
        #)))
        #print("Close button found.")

        ## Scroll to the button before clicking it
        #driver.execute_script("arguments[0].scrollIntoView(true);", close_button)
        #time.sleep(1)

        ## Click the close button
        #driver.execute_script("arguments[0].click();", close_button)
        #print("Modal closed.")
        #time.sleep(1)

        # --- Q2 ---
        Q2_td = wait.until(EC.element_to_be_clickable((
            By.XPATH,
            '//*[@id="tbl-icq-findings-body"]/tr[10]/td[2]/span'
        )))
        driver.execute_script("arguments[0].scrollIntoView(true);", Q2_td)
        Q2_td.click()
        print("Clicked on 'Q2'.")
        time.sleep(1)

        try:
            # --- Validation: Check if FND Yes/No radio is selected ---
            fnd_yes_radio = driver.find_element(By.ID, "fndYes")  # replace with actual ID
            assert fnd_yes_radio.is_selected(), "'Yes, No, N.A' is not selected."

            print("Required FND selection made. Proceeding to save.")

            # --- Save button click ---
            save_button = wait.until(EC.element_to_be_clickable((By.ID, "addIcqYesNoRemarks")))
            driver.execute_script("arguments[0].scrollIntoView(true);", save_button)
            time.sleep(0.5)

            actions = ActionChains(driver)
            actions.move_to_element(save_button).click().perform()

            print("Save button clicked successfully.")

        except AssertionError as ae:
            print(f"Assertion Error: {ae}")

        except Exception as e:
            print(f"Unexpected error: {e}")

        # --- Wait for Modal to be Visible ---
        try:
            Internal = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="AddIcqYesNoModal"]')))
            print("Modal is visible.")
            time.sleep(1)

            # --- Wait for Close Button and Click It ---
            try:
                close_button = wait.until(EC.element_to_be_clickable((
                    By.XPATH, '//*[@id="AddIcqYesNoModal"]/div/div/div[1]/button'
                )))
                print("Close button found.")

                # Scroll to the button before clicking it
                driver.execute_script("arguments[0].scrollIntoView(true);", close_button)
                time.sleep(1)

                # Click the close button
                driver.execute_script("arguments[0].click();", close_button)
                print("Q2 Modal closed.")
                time.sleep(1)

            except Exception as e:
                print(f"Failed to click the close button: {e}")
                print("Proceeding to the next step.")

        except Exception as e:
            print(f"Modal not visible or failed to load: {e}")
            print("Proceeding without modal interaction.")

        # --- Book Icon (Safe with Assertion, Minimal Print) ---
        try:
            # Wait for the book element to appear
            book = wait.until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="tbl-icq-findings-body"]/tr[9]/td[2]/div'))
            )

            # Assert it's displayed and enabled
            assert book.is_displayed(), "Book icon button is not visible on the page."
            assert book.is_enabled(), "Book icon button is not enabled for clicking."

            # Scroll and click
            driver.execute_script("arguments[0].scrollIntoView(true);", book)
            time.sleep(0.5)
            book.click()
            print("Book icon button clicked.")

        except AssertionError as ae:
            print(f"Assertion Error: {ae}")

        except Exception:
            pass  # Fail silently on non-assertion exceptions

        finally:
            time.sleep(1)

            # --- Comment Icon Button (Safe with Assertion, Minimal Print) ---
            try:
                # Wait for the comment element to appear
                comment = wait.until(EC.presence_of_element_located((
                    By.XPATH, '//a[@class="text-dark comments" and @data-fnd-id="175"]'
                )))

                # Assert it's displayed and enabled
                assert comment.is_displayed(), "Comment icon button is not visible on the page."
                assert comment.is_enabled(), "Comment icon button is not enabled for clicking."

                # Scroll and click
                driver.execute_script("arguments[0].scrollIntoView(true);", comment)
                time.sleep(0.5)
                comment.click()
                print("Comment icon button clicked.")

            except AssertionError as ae:
                print(f"Assertion Error: {ae}")

            except Exception:
                pass  # Silently ignore non-assertion exceptions

            finally:
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
