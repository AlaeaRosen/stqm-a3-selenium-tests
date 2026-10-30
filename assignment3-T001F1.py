import selenium 
from selenium import webdriver 
import time 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# TEST CASE 1 - USER LOGIN FROM HOME PAGE
        # Scenario 1: Valid

#Step 1: Enter the website
driver = webdriver.Safari()
driver.get("https://opencart.abstracta.us/index.php?route=common/home")

wait = WebDriverWait(driver, 10)
wait.until(lambda d: d.execute_script("return document.readyState") == "complete")

#Step 2: Click on My Account, and then Login
button_myAccount = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"a[title='My Account']")))
button_myAccount.click()

button_login1 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"a[href*='account/login']")))
button_login1.click()

element = wait.until(EC.presence_of_element_located((By.ID,"account-login")))

#Step 3: Put a correct Email
text_email = driver.find_element(By.XPATH,"//input[@type = 'text' and @name = 'email' and @placeholder='E-Mail Address' and @id='input-email']")
text_email.send_keys("emily1@test.com")
print(text_email.get_attribute("value"))
assert text_email.get_attribute("value") == "emily1@test.com"

#Step 4: Put a correct password
text_password = driver.find_element(By.ID,"input-password")
text_password.send_keys("Pass")
print(text_password.get_attribute("value"))
assert text_password.get_attribute("value") == "Pass"

#Step 5: Click Login button
button_login2 = wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@type = 'submit' and @value = 'Login']")))
button_login2.click()

redirected = wait.until(EC.url_contains("account/account"))

text_myAccount = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"a[href*='account/edit']")))
assert "My Orders" in driver.find_element(By.TAG_NAME, "body").text

time.sleep(10)
driver.quit()

        #  Scenario 2: Unregistered email

#Step 1: Enter the website
driver = webdriver.Safari()
driver.get("https://opencart.abstracta.us/index.php?route=common/home")

wait = WebDriverWait(driver, 10)
wait.until(lambda d: d.execute_script("return document.readyState") == "complete")

#Step 2: Click on My Account, and then Login
button_myAccount = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"a[title='My Account']")))
button_myAccount.click()

button_login1 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"a[href*='account/login']")))
button_login1.click()

element = wait.until(EC.presence_of_element_located((By.ID,"account-login")))

#Step 3: Put an unregistered Email
text_email = driver.find_element(By.XPATH,"//input[@type = 'text' and @name = 'email' and @placeholder='E-Mail Address' and @id='input-email']")
text_email.send_keys("emily@what.com")
print(text_email.get_attribute("value"))
assert text_email.get_attribute("value") == "emily@what.com"

#Step 4: Put a correct password
text_password = driver.find_element(By.ID,"input-password")
text_password.send_keys("Pass")
print(text_password.get_attribute("value"))
assert text_password.get_attribute("value") == "Pass"

#Step 5: Click Login button
button_login2 = wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@type = 'submit' and @value = 'Login']")))
button_login2.click()

warning = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,".alert-danger")))
assert "No match for E-Mail Address and/or Password." in warning.text

time.sleep(10)
driver.quit()

        # Scenario 3: Incorrect password

#Step 1: Enter the website
driver = webdriver.Safari()
driver.get("https://opencart.abstracta.us/index.php?route=common/home")
wait = WebDriverWait(driver, 10)
wait.until(lambda d: d.execute_script("return document.readyState") == "complete")

#Step 2: Click on My Account, and then Login
button_myAccount = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"a[title='My Account']")))
button_myAccount.click()

button_login1 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"a[href*='account/login']")))
button_login1.click()

element = wait.until(EC.presence_of_element_located((By.ID,"account-login")))

#Step 3: Put a correct Email
text_email = driver.find_element(By.XPATH,"//input[@type = 'text' and @name = 'email' and @placeholder='E-Mail Address' and @id='input-email']")
text_email.send_keys("emily1@test.com")
print(text_email.get_attribute("value"))
assert text_email.get_attribute("value") == "emily1@test.com"

#Step 4: Put an incorrect password
text_password = driver.find_element(By.ID,"input-password")
text_password.send_keys("Password!")
print(text_password.get_attribute("value"))
assert text_password.get_attribute("value") == "Password!"

#Step 5: Click Login button
button_login2 = wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@type = 'submit' and @value = 'Login']")))
button_login2.click()

warning = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,".alert-danger")))
assert "No match for E-Mail Address and/or Password." in warning.text

time.sleep(10)
driver.quit()

        # Scenario 4: Forgotten password - Valid

#Step 1: Enter the website
driver = webdriver.Safari()
driver.get("https://opencart.abstracta.us/index.php?route=common/home")

wait = WebDriverWait(driver, 10)
wait.until(lambda d: d.execute_script("return document.readyState") == "complete")

#Step 2: Click on My Account, and then Login
button_myAccount = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"a[title='My Account']")))
button_myAccount.click()

button_login1 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"a[href*='account/login']")))
button_login1.click()

element = wait.until(EC.presence_of_element_located((By.ID,"account-login")))

#Step 3: Click Forgotten Password button
button_forgotten = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"a[href*='account/forgotten']")))
button_forgotten.click()

forgotten_page = wait.until(EC.presence_of_element_located((By.ID,"account-forgotten")))

#Step 4: Put an Email
text_email = driver.find_element(By.XPATH,"//input[@type = 'text' and @name = 'email' and @placeholder='E-Mail Address' and @id='input-email']")
text_email.send_keys("emily1@test.com")
print(text_email.get_attribute("value"))
assert text_email.get_attribute("value") == "emily1@test.com"

#Step 5: Click Continue button
button_continue = wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@type = 'submit' and @value = 'Continue']")))
button_continue.click()

redirected = wait.until(EC.url_contains("account/login"))

text_confirmation = wait.until(EC.visibility_of_element_located((By.CLASS_NAME,"alert-success")))
assert "An email with a confirmation link has been sent your email address" in text_confirmation.text

time.sleep(10)
driver.quit()

        #   Scenario 5: Forgotten Password - Incorrect Email 

#Step 1: Enter the website
driver = webdriver.Safari()
driver.get("https://opencart.abstracta.us/index.php?route=common/home")

wait = WebDriverWait(driver, 10)
wait.until(lambda d: d.execute_script("return document.readyState") == "complete")

#Step 2: Click on My Account, and then Login
button_myAccount = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"a[title='My Account']")))
button_myAccount.click()

button_login1 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"a[href*='account/login']")))
button_login1.click()

element = wait.until(EC.presence_of_element_located((By.ID,"account-login")))

#Step 3: Click Forgotten Password button
button_forgotten = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"a[href*='account/forgotten']")))
button_forgotten.click()

forgotten_page = wait.until(EC.presence_of_element_located((By.ID,"account-forgotten")))

#Step 4: Put an Email
text_email = driver.find_element(By.XPATH,"//input[@type = 'text' and @name = 'email' and @placeholder='E-Mail Address' and @id='input-email']")
text_email.send_keys("1233254245435563.f@example.com")
print(text_email.get_attribute("value"))
assert text_email.get_attribute("value") == "1233254245435563.f@example.com"

#Step 5: Click Continue button
button_continue = wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@type = 'submit' and @value = 'Continue']")))
button_continue.click()

warning = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,".alert-danger")))
assert "The E-Mail Address was not found in our records, please try again" in warning.text

time.sleep(10)
driver.quit()