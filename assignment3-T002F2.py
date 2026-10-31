import selenium 
from selenium import webdriver 
import time 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# TEST CASE 2 - USER REGISTRATION FROM HOME PAGE
      # Scenario 1: Valid

#Step 1: Enter the website
driver = webdriver.Safari()
driver.get("https://opencart.abstracta.us/index.php?route=common/home")

wait = WebDriverWait(driver, 10)
wait.until(lambda d: d.execute_script("return document.readyState") == "complete")

#Step 2: Click on My Account, and then Register
button_myAccount = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"a[title='My Account']")))
button_myAccount.click()

button_register = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"a[href*='account/register']")))
button_register.click()

element = wait.until(EC.presence_of_element_located((By.ID,"input-firstname")))

#Step 3: Add First Name
text_firstname = driver.find_element(By.ID,"input-firstname")
text_firstname.send_keys("Emily")
print(text_firstname.get_attribute("value"))
assert text_firstname.get_attribute("value") == "Emily"

#Step 4: Add Last Name
text_lastname = driver.find_element(By.ID,"input-lastname")
text_lastname.send_keys("Fons")
print(text_lastname.get_attribute("value"))
assert text_lastname.get_attribute("value") == "Fons"

#Step 5: Add Email
text_email = driver.find_element(By.ID,"input-email")
text_email.send_keys("emily.fons@example.com")
print(text_email.get_attribute("value"))
assert text_email.get_attribute("value") == "emily.fons@example.com"

#Step 6: Add Telephone
text_telephone = driver.find_element(By.ID,"input-telephone")
text_telephone.send_keys("0400100100")
print(text_telephone.get_attribute("value"))
assert text_telephone.get_attribute("value") == "0400100100"

#Step 7: Add Password
text_password = driver.find_element(By.ID,"input-password")
text_password.send_keys("Password!12")
print(text_password.get_attribute("value"))
assert text_password.get_attribute("value") == "Password!12"

#Step 8: Add Password Confirm
text_confirm = driver.find_element(By.ID,"input-confirm")
text_confirm.send_keys("Password!12")
print(text_confirm.get_attribute("value"))
assert text_confirm.get_attribute("value") == "Password!12"

#Step 9: Select Yes to Subscribe Newsletter
subscribe_radio = driver.find_element(By.XPATH,"//input[@type = 'radio' and @name = 'newsletter' and @value = '1']")
subscribe_radio.click()
assert subscribe_radio.is_selected()

#Step 10: Select "I have read and agree to the Privacy Policy" checkbox
agree_checkbox = driver.find_element(By.XPATH,"//input[@type = 'checkbox' and @name = 'agree' and @value = '1']")
agree_checkbox.click()
assert agree_checkbox.is_selected()

#Step 11: Click Continue button
submit_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@type = 'submit' and @value = 'Continue']")))
submit_button.click()
 
redirected = wait.until(EC.url_contains("account/success"))
assert "Your new account has been successfully created" in driver.find_element(By.TAG_NAME, "body").text

time.sleep(10)
driver.quit()

      # Scenario 2: 1 Missing value - First Name

#Step 1: Enter the website
driver = webdriver.Safari()
driver.get("https://opencart.abstracta.us/index.php?route=common/home")

wait = WebDriverWait(driver, 10)
wait.until(lambda d: d.execute_script("return document.readyState") == "complete")

#Step 2: Click on My Account, and then Register
button_myAccount = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"a[title='My Account']")))
button_myAccount.click()

button_register = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"a[href*='account/register']")))
button_register.click()

element = wait.until(EC.presence_of_element_located((By.ID,"input-firstname")))

#Step 3: Add Last Name
text_lastname = driver.find_element(By.ID,"input-lastname")
text_lastname.send_keys("Fons")
print(text_lastname.get_attribute("value"))
assert text_lastname.get_attribute("value") == "Fons"

#Step 4: Add Email
text_email = driver.find_element(By.ID,"input-email")
text_email.send_keys("emily.fons3@example.com")
print(text_email.get_attribute("value"))
assert text_email.get_attribute("value") == "emily.fons3@example.com"

#Step 5: Add Telephone
text_telephone = driver.find_element(By.ID,"input-telephone")
text_telephone.send_keys("0400100100")
print(text_telephone.get_attribute("value"))
assert text_telephone.get_attribute("value") == "0400100100"

#Step 6: Add Password
text_password = driver.find_element(By.ID,"input-password")
text_password.send_keys("Password!12")
print(text_password.get_attribute("value"))
assert text_password.get_attribute("value") == "Password!12"

#Step 7: Add Password Confirm
text_confirm = driver.find_element(By.ID,"input-confirm")
text_confirm.send_keys("Password!12")
print(text_confirm.get_attribute("value"))
assert text_confirm.get_attribute("value") == "Password!12"

#Step 8: Select Yes to Subscribe Newsletter
subscribe_radio = driver.find_element(By.XPATH,"//input[@type = 'radio' and @name = 'newsletter' and @value = '1']")
subscribe_radio.click()
assert subscribe_radio.is_selected()

#Step 9: Select "I have read and agree to the Privacy Policy" checkbox
agree_checkbox = driver.find_element(By.XPATH,"//input[@type = 'checkbox' and @name = 'agree' and @value = '1']")
agree_checkbox.click()
assert agree_checkbox.is_selected()

#Step 10: Click Continue button
submit_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@type = 'submit' and @value = 'Continue']")))
submit_button.click()
 
warning = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,".text-danger")))
assert "First Name must be between 1 and 32 characters!" in warning.text

time.sleep(10)
driver.quit()

        # Scenario 3: Password and Password Confirm not the same

#Step 1: Enter the website
driver = webdriver.Safari()
driver.get("https://opencart.abstracta.us/index.php?route=common/home")

wait = WebDriverWait(driver, 10)
wait.until(lambda d: d.execute_script("return document.readyState") == "complete")

#Step 2: Click on My Account, and then Register
button_myAccount = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"a[title='My Account']")))
button_myAccount.click()

button_register = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"a[href*='account/register']")))
button_register.click()

element = wait.until(EC.presence_of_element_located((By.ID,"input-firstname")))

#Step 3: Add First Name
text_firstname = driver.find_element(By.ID,"input-firstname")
text_firstname.send_keys("Emily")
print(text_firstname.get_attribute("value"))
assert text_firstname.get_attribute("value") == "Emily"

#Step 4: Add Last Name
text_lastname = driver.find_element(By.ID,"input-lastname")
text_lastname.send_keys("Fons")
print(text_lastname.get_attribute("value"))
assert text_lastname.get_attribute("value") == "Fons"

#Step 5: Add Email
text_email = driver.find_element(By.ID,"input-email")
text_email.send_keys("emily.fons4@example.com")
print(text_email.get_attribute("value"))
assert text_email.get_attribute("value") == "emily.fons4@example.com"

#Step 6: Add Telephone
text_telephone = driver.find_element(By.ID,"input-telephone")
text_telephone.send_keys("0400100100")
print(text_telephone.get_attribute("value"))
assert text_telephone.get_attribute("value") == "0400100100"

#Step 7: Add Password
text_password = driver.find_element(By.ID,"input-password")
text_password.send_keys("Password!12")
print(text_password.get_attribute("value"))
assert text_password.get_attribute("value") == "Password!12"

#Step 8: Put the wrong Password Confirm
text_confirm = driver.find_element(By.ID,"input-confirm")
text_confirm.send_keys("Password!1234")
print(text_confirm.get_attribute("value"))
assert text_confirm.get_attribute("value") == "Password!1234"

#Step 9: Select Yes to Subscribe Newsletter
subscribe_radio = driver.find_element(By.XPATH,"//input[@type = 'radio' and @name = 'newsletter' and @value = '1']")
subscribe_radio.click()
assert subscribe_radio.is_selected()

#Step 10: Select "I have read and agree to the Privacy Policy" checkbox
agree_checkbox = driver.find_element(By.XPATH,"//input[@type = 'checkbox' and @name = 'agree' and @value = '1']")
agree_checkbox.click()
assert agree_checkbox.is_selected()

#Step 11: Click Continue button
submit_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@type = 'submit' and @value = 'Continue']")))
submit_button.click()
 
warning = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,".text-danger")))
assert "Password confirmation does not match password" in warning.text

time.sleep(10)
driver.quit()

        # Scenario 4: Email invalid format

#Step 1: Enter the website
driver = webdriver.Safari()
driver.get("https://opencart.abstracta.us/index.php?route=common/home")

wait = WebDriverWait(driver, 10)
wait.until(lambda d: d.execute_script("return document.readyState") == "complete")

#Step 2: Click on My Account, and then Register
button_myAccount = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"a[title='My Account']")))
button_myAccount.click()

button_register = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"a[href*='account/register']")))
button_register.click()

element = wait.until(EC.presence_of_element_located((By.ID,"input-firstname")))

#Step 3: Add First Name
text_firstname = driver.find_element(By.ID,"input-firstname")
text_firstname.send_keys("Emily")
print(text_firstname.get_attribute("value"))
assert text_firstname.get_attribute("value") == "Emily"

#Step 4: Add Last Name
text_lastname = driver.find_element(By.ID,"input-lastname")
text_lastname.send_keys("Fons")
print(text_lastname.get_attribute("value"))
assert text_lastname.get_attribute("value") == "Fons"

#Step 5: Put an invalid Email
text_email = driver.find_element(By.ID,"input-email")
text_email.send_keys("emily.com")
print(text_email.get_attribute("value"))
assert text_email.get_attribute("value") == "emily.com"

#Step 6: Add Telephone
text_telephone = driver.find_element(By.ID,"input-telephone")
text_telephone.send_keys("0400100100")
print(text_telephone.get_attribute("value"))
assert text_telephone.get_attribute("value") == "0400100100"

#Step 7: Add Password
text_password = driver.find_element(By.ID,"input-password")
text_password.send_keys("Password!12")
print(text_password.get_attribute("value"))
assert text_password.get_attribute("value") == "Password!12"

#Step 8: Add Password Confirm
text_confirm = driver.find_element(By.ID,"input-confirm")
text_confirm.send_keys("Password!12")
print(text_confirm.get_attribute("value"))
assert text_confirm.get_attribute("value") == "Password!12"

#Step 9: Select Yes to Subscribe Newsletter
subscribe_radio = driver.find_element(By.XPATH,"//input[@type = 'radio' and @name = 'newsletter' and @value = '1']")
subscribe_radio.click()
assert subscribe_radio.is_selected()

#Step 10: Select "I have read and agree to the Privacy Policy" checkbox
agree_checkbox = driver.find_element(By.XPATH,"//input[@type = 'checkbox' and @name = 'agree' and @value = '1']")
agree_checkbox.click()
assert agree_checkbox.is_selected()

#Step 11: Click Continue button
submit_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@type = 'submit' and @value = 'Continue']")))
submit_button.click()
 
message = text_email.get_attribute("validationMessage")
print(message)
assert message != ""

time.sleep(10)
driver.quit()

        # Scenario 5: Privacy Policy not ticked

#Step 1: Enter the website
driver = webdriver.Safari()
driver.get("https://opencart.abstracta.us/index.php?route=common/home")

wait = WebDriverWait(driver, 10)
wait.until(lambda d: d.execute_script("return document.readyState") == "complete")

#Step 2: Click on My Account, and then Register
button_myAccount = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"a[title='My Account']")))
button_myAccount.click()

button_register = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"a[href*='account/register']")))
button_register.click()

element = wait.until(EC.presence_of_element_located((By.ID,"input-firstname")))

#Step 3: Add First Name
text_firstname = driver.find_element(By.ID,"input-firstname")
text_firstname.send_keys("Emily")
print(text_firstname.get_attribute("value"))
assert text_firstname.get_attribute("value") == "Emily"

#Step 4: Add Last Name
text_lastname = driver.find_element(By.ID,"input-lastname")
text_lastname.send_keys("Fons")
print(text_lastname.get_attribute("value"))
assert text_lastname.get_attribute("value") == "Fons"

#Step 5: Add Email
text_email = driver.find_element(By.ID,"input-email")
text_email.send_keys("emily.fons5@test.com")
print(text_email.get_attribute("value"))
assert text_email.get_attribute("value") == "emily.fons5@test.com"

#Step 6: Add Telephone
text_telephone = driver.find_element(By.ID,"input-telephone")
text_telephone.send_keys("0400100100")
print(text_telephone.get_attribute("value"))
assert text_telephone.get_attribute("value") == "0400100100"

#Step 7: Add Password
text_password = driver.find_element(By.ID,"input-password")
text_password.send_keys("Password!12")
print(text_password.get_attribute("value"))
assert text_password.get_attribute("value") == "Password!12"

#Step 8: Add Password Confirm
text_confirm = driver.find_element(By.ID,"input-confirm")
text_confirm.send_keys("Password!12")
print(text_confirm.get_attribute("value"))
assert text_confirm.get_attribute("value") == "Password!12"

#Step 9: Select Yes to Subscribe Newsletter
subscribe_radio = driver.find_element(By.XPATH,"//input[@type = 'radio' and @name = 'newsletter' and @value = '1']")
subscribe_radio.click()
assert subscribe_radio.is_selected()

#Step 10: Click Continue button
submit_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@type = 'submit' and @value = 'Continue']")))
submit_button.click()
 
warning = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,".alert-danger")))
assert "You must agree to the Privacy Policy" in warning.text

time.sleep(10)
driver.quit()

        # Scenario 6: Existing email

#Step 1: Enter the website
driver = webdriver.Safari()
driver.get("https://opencart.abstracta.us/index.php?route=common/home")

wait = WebDriverWait(driver, 10)
wait.until(lambda d: d.execute_script("return document.readyState") == "complete")

#Step 2: Click on My Account, and then Register
button_myAccount = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"a[title='My Account']")))
button_myAccount.click()

button_register = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"a[href*='account/register']")))
button_register.click()

element = wait.until(EC.presence_of_element_located((By.ID,"input-firstname")))

#Step 3: Add First Name
text_firstname = driver.find_element(By.ID,"input-firstname")
text_firstname.send_keys("Emily")
print(text_firstname.get_attribute("value"))
assert text_firstname.get_attribute("value") == "Emily"

#Step 4: Add Last Name
text_lastname = driver.find_element(By.ID,"input-lastname")
text_lastname.send_keys("Fons")
print(text_lastname.get_attribute("value"))
assert text_lastname.get_attribute("value") == "Fons"

#Step 5: Put an existing Email
text_email = driver.find_element(By.ID,"input-email")
text_email.send_keys("test@example.com")
print(text_email.get_attribute("value"))
assert text_email.get_attribute("value") == "test@example.com"

#Step 6: Add Telephone
text_telephone = driver.find_element(By.ID,"input-telephone")
text_telephone.send_keys("0400100100")
print(text_telephone.get_attribute("value"))
assert text_telephone.get_attribute("value") == "0400100100"

#Step 7: Add Password
text_password = driver.find_element(By.ID,"input-password")
text_password.send_keys("Password!12")
print(text_password.get_attribute("value"))
assert text_password.get_attribute("value") == "Password!12"

#Step 8: Add Password Confirm
text_confirm = driver.find_element(By.ID,"input-confirm")
text_confirm.send_keys("Password!12")
print(text_confirm.get_attribute("value"))
assert text_confirm.get_attribute("value") == "Password!12"

#Step 9: Select Yes to Subscribe Newsletter
subscribe_radio = driver.find_element(By.XPATH,"//input[@type = 'radio' and @name = 'newsletter' and @value = '1']")
subscribe_radio.click()
assert subscribe_radio.is_selected()

#Step 10: Select "I have read and agree to the Privacy Policy" checkbox
agree_checkbox = driver.find_element(By.XPATH,"//input[@type = 'checkbox' and @name = 'agree' and @value = '1']")
agree_checkbox.click()
assert agree_checkbox.is_selected()

#Step 11: Click Continue button
submit_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@type = 'submit' and @value = 'Continue']")))
submit_button.click()
 
warning = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,".alert-danger")))
assert "E-Mail Address is already registered" in warning.text

time.sleep(10)
driver.quit()

        # Scenario 7: Short Password 

#Step 1: Enter the website
driver = webdriver.Safari()
driver.get("https://opencart.abstracta.us/index.php?route=common/home")

wait = WebDriverWait(driver, 10)
wait.until(lambda d: d.execute_script("return document.readyState") == "complete")

#Step 2: Click on My Account, and then Register
button_myAccount = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"a[title='My Account']")))
button_myAccount.click()

button_register = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"a[href*='account/register']")))
button_register.click()

element = wait.until(EC.presence_of_element_located((By.ID,"input-firstname")))

#Step 3: Add First Name
text_firstname = driver.find_element(By.ID,"input-firstname")
text_firstname.send_keys("Emily")
print(text_firstname.get_attribute("value"))
assert text_firstname.get_attribute("value") == "Emily"

#Step 4: Add Last Name
text_lastname = driver.find_element(By.ID,"input-lastname")
text_lastname.send_keys("Fons")
print(text_lastname.get_attribute("value"))
assert text_lastname.get_attribute("value") == "Fons"

#Step 5: Add Email
text_email = driver.find_element(By.ID,"input-email")
text_email.send_keys("emily11@test.com")
print(text_email.get_attribute("value"))
assert text_email.get_attribute("value") == "emily11@test.com"

#Step 6: Add Telephone
text_telephone = driver.find_element(By.ID,"input-telephone")
text_telephone.send_keys("0400100100")
print(text_telephone.get_attribute("value"))
assert text_telephone.get_attribute("value") == "0400100100"

#Step 7: Add Weak Password
text_password = driver.find_element(By.ID,"input-password")
text_password.send_keys("Pass")
print(text_password.get_attribute("value"))
assert text_password.get_attribute("value") == "Pass"

#Step 8: Add Short Password Confirm
text_confirm = driver.find_element(By.ID,"input-confirm")
text_confirm.send_keys("Pass")
print(text_confirm.get_attribute("value"))
assert text_confirm.get_attribute("value") == "Pass"

#Step 9: Select Yes to Subscribe Newsletter
subscribe_radio = driver.find_element(By.XPATH,"//input[@type = 'radio' and @name = 'newsletter' and @value = '1']")
subscribe_radio.click()
assert subscribe_radio.is_selected()

#Step 10: Select "I have read and agree to the Privacy Policy" checkbox
agree_checkbox = driver.find_element(By.XPATH,"//input[@type = 'checkbox' and @name = 'agree' and @value = '1']")
agree_checkbox.click()
assert agree_checkbox.is_selected()

#Step 11: Click Continue button
submit_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@type = 'submit' and @value = 'Continue']")))
submit_button.click()

wait.until(lambda d: "account/success" in d.current_url or d.find_elements(By.CSS_SELECTOR, ".alert.danger, .text.danger"))
 
assert "account/success" not in driver.current_url, "Weak Password 'Pass' was accepted: account created"

time.sleep(10)
driver.quit()