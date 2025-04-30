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
    # --- Print table content ---
    print("Table content:")
    print(tbody.text)

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
    comment_box.send_keys("Technology is the bridge between imagination and reality, turning dreams into everyday experiences.")
    print("Comment entered successfully.")
    time.sleep(1)

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
    print(" Modal closed .")
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
    print(" Modal closed .")
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
    print(" Modal closed .")
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

    # --- File ---
    #File_td = wait.until(EC.element_to_be_clickable((
        #By.XPATH,
        #'//*[@id="fndRemarks"]/div[2]/div[1]/div[1]/div[2]/button[1]'
    #)))
    #driver.execute_script("arguments[0].scrollIntoView(true);", File_td)
    #File_td.click()
    #print("Clicked on 'File'.")
    #time.sleep(1)

    # --- Edit ---
    #Edit_td = wait.until(EC.element_to_be_clickable((
        #By.XPATH,
        #'//*[@id="fndRemarks"]/div[2]/div[1]/div[1]/div[2]/button[2]'
    #)))
    #driver.execute_script("arguments[0].scrollIntoView(true);", Edit_td)
    #Edit_td.click()
    #print("Clicked on 'Edit'.")
    #time.sleep(1)

    # --- View ---
    #View_td = wait.until(EC.element_to_be_clickable((
        #By.XPATH,
        #'//*[@id="fndRemarks"]/div[2]/div[1]/div[1]/div[2]/button[3]'
    #)))
    #driver.execute_script("arguments[0].scrollIntoView(true);", View_td)
    #View_td.click()
    #print("Clicked on 'View'.")
    #time.sleep(1)

    # --- Insert ---
    #Insert_td = wait.until(EC.element_to_be_clickable((
        #By.XPATH,
        #'//*[@id="fndRemarks"]/div[2]/div[1]/div[1]/div[2]/button[4]'
    #)))
    #driver.execute_script("arguments[0].scrollIntoView(true);", Insert_td)
    #Insert_td.click()
    #print("Clicked on 'Insert'.")
    #time.sleep(1)

    # --- Format ---
    #Format_td = wait.until(EC.element_to_be_clickable((
        #By.XPATH,
        #'//*[@id="fndRemarks"]/div[2]/div[1]/div[1]/div[2]/button[5]'
    #)))
    #driver.execute_script("arguments[0].scrollIntoView(true);", Format_td)
    #Format_td.click()
    #print("Clicked on 'Format'.")
    #time.sleep(1)

    # --- Tools ---
    #Tools_td = wait.until(EC.element_to_be_clickable((
        #By.XPATH,
        #'//*[@id="fndRemarks"]/div[2]/div[1]/div[1]/div[2]/button[6]'
    #)))
    #driver.execute_script("arguments[0].scrollIntoView(true);", Tools_td)
    #Tools_td.click()
    #print("Clicked on 'Tools'.")
    #time.sleep(1)

    # --- Table---
    #Tabletd = wait.until(EC.element_to_be_clickable((
        #By.XPATH,
        #'//*[@id="fndRemarks"]/div[2]/div[1]/div[1]/div[2]/button[7]'
    #)))
    #driver.execute_script("arguments[0].scrollIntoView(true);", Tabletd)
    #Tabletd.click()
    #time.sleep(1)

    # --- Table Button Click ---
    #try:
        #Table_td = wait.until(EC.element_to_be_clickable((
            #By.XPATH,
            #'//*[@id="fndRemarks"]/div[2]/div[1]/div[1]/div[2]/button[7]'
        #)))

        #driver.execute_script("arguments[0].scrollIntoView(true);", Table_td)
        #time.sleep(0.5)  # Short sleep to allow any animations

        #Table_td.click()
        #print("Clicked on 'Table' button.")

    #except Exception as e:
        #print(f"Error clicking on 'Table' button: {e}")

    #finally:
        #print("Proceeding to the next step after attempting to click 'Table'.")

        # --- Enter Remarks in TinyMCE iframe ---
        remarks_iframe = wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, "fnd_remarks1_ifr")))
        remarks_body = wait.until(EC.presence_of_element_located((By.ID, "tinymce")))
        remarks_body.clear()
        remarks_body.send_keys("Hello World")
        print("Remarks entered successfully.")
        time.sleep(1)
        driver.switch_to.default_content()

        ## --- Undo---
        #Undotd = wait.until(EC.element_to_be_clickable((
            #By.XPATH,
            #'//*[@id="fndRemarks"]/div[2]/div[1]/div[1]/div[3]/div/div[1]/button[1]'
        #)))
        #driver.execute_script("arguments[0].scrollIntoView(true);", Undotd)
        #Undotd.click()
        #print("Undo button clicked.")
        #time.sleep(1)

        ## ---Redo---
        #Redotd = wait.until(EC.element_to_be_clickable((
            #By.XPATH,
            #'//*[@id="fndRemarks"]/div[2]/div[1]/div[1]/div[3]/div/div[1]/button[2]'
        #)))
        #driver.execute_script("arguments[0].scrollIntoView(true);", Redotd)
        #Redotd.click()
        #print("Redo button clicked.")
        #time.sleep(1)

        ## --- Paragraph Format ---
        #paragraph_btn = wait.until(EC.element_to_be_clickable((
            #By.XPATH,
            #'//*[@id="fndRemarks"]/div[2]/div[1]/div[1]/div[3]/div/div[2]/button'
        #)))
        #driver.execute_script("arguments[0].scrollIntoView(true);", paragraph_btn)
        #paragraph_btn.click()
        #print("Paragraph formatting button clicked.")
        #time.sleep(1)

        ## --- Bold / Italic / Underline Buttons ---
        #try:
            ## Base toolbar group
            #toolbar_group = wait.until(EC.presence_of_element_located((
                #By.XPATH, '//*[@id="fndRemarks"]/div[2]/div[1]/div[1]/div[3]/div/div[3]'
            #)))
            #driver.execute_script("arguments[0].scrollIntoView(true);", toolbar_group)

            ## Buttons are ordered: Bold, Italic, Underline
            #buttons = toolbar_group.find_elements(By.TAG_NAME, "button")

            #if len(buttons) >= 3:
                ## Bold
                #buttons[0].click()
                #print("Bold button clicked.")
                #time.sleep(1)

                ## Italic
                #buttons[1].click()
                #print("Italic button clicked.")
                #time.sleep(1)

                ## Underline
                #buttons[2].click()
                #print("Underline button clicked.")
                #time.sleep(1)
            #else:
                #print("Expected Bold/Italic/Underline buttons not found.")
        #except Exception as e:
           # print(f"Error interacting with formatting buttons: {e}")

            ## --- Toolbar Items ---
            #toolbar_items = wait.until(EC.element_to_be_clickable((
               # By.XPATH,
                #'//*[@id="fndRemarks"]/div[2]/div[1]/div[1]/div[3]/div/div[4]/button'
            #)))
            #driver.execute_script("arguments[0].scrollIntoView(true);", toolbar_items)
           # toolbar_items.click()
            #print("Toolbar item clicked.")
            #time.sleep(1)

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
                print("Modal closed.")
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
