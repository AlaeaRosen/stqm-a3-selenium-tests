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

#Step 2: Click on My Account, and then Register
button_myAccount = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"a[title='My Account']")))
button_myAccount.click()

button_login1 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"a[href*='account/login']")))
button_login1.click()

element = wait.until(EC.presence_of_element_located((By.ID,"account-login")))

#Step 3: Put a correct Email
text_email = driver.find_element(By.XPATH,"//input[@type = 'text' and @name = 'email' and @placeholder='E-Mail Address' and @id='input-email']")
text_email.send_keys("emily1@test.com")
print(text_email.get_attribute("Value"))
assert text_email is not None
assert text_email.get_attribute("value") == "emily1@test.com"

#Step 4: Put a correct password
text_password = driver.find_element(By.ID,"input-password")
text_password.send_keys("Pass")
print(text_password.get_attribute("Value"))
assert text_password is not None
assert text_password.get_attribute("value") == "Pass"

#Step 5: Click Login button
button_login2 = wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@type = 'submit' and @value = 'Login']")))
button_login2.click()

text_myAccount = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"a[href*='account/edit']")))

        #  Scenario 2: Incorrect email

#Step 1: Enter the website
driver = webdriver.Safari()
driver.get("https://opencart.abstracta.us/index.php?route=common/home")

wait = WebDriverWait(driver, 10)

#Step 2: Click on My Account, and then Register
button_myAccount = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"a[title='My Account']")))
button_myAccount.click()

button_login1 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"a[href*='account/login']")))
button_login1.click()

element = wait.until(EC.presence_of_element_located((By.ID,"account-login")))

#Step 3: Put an incorrect Email
text_email = driver.find_element(By.XPATH,"//input[@type = 'text' and @name = 'email' and @placeholder='E-Mail Address' and @id='input-email']")
text_email.send_keys("emily@what.com")
print(text_email.get_attribute("Value"))
assert text_email is not None
assert text_email.get_attribute("value") == "emily@what.com"

#Step 4: Put a correct password
text_password = driver.find_element(By.ID,"input-password")
text_password.send_keys("Pass")
print(text_password.get_attribute("Value"))
assert text_password is not None
assert text_password.get_attribute("value") == "Pass"

#Step 5: Click Login button
button_login2 = wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@type = 'submit' and @value = 'Login']")))
button_login2.click()

text_myAccount = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"a[href*='account/edit']")))

        # Scenario 3: Incorrect password

#Step 1: Enter the website
driver = webdriver.Safari()
driver.get("https://opencart.abstracta.us/index.php?route=common/home")

wait = WebDriverWait(driver, 10)

#Step 2: Click on My Account, and then Register
button_myAccount = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"a[title='My Account']")))
button_myAccount.click()

button_login1 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"a[href*='account/login']")))
button_login1.click()

element = wait.until(EC.presence_of_element_located((By.ID,"account-login")))

#Step 3: Put an correct Email
text_email = driver.find_element(By.XPATH,"//input[@type = 'text' and @name = 'email' and @placeholder='E-Mail Address' and @id='input-email']")
text_email.send_keys("emily1@test.com")
print(text_email.get_attribute("Value"))
assert text_email is not None
assert text_email.get_attribute("value") == "emily1@test.com"

#Step 4: Put a correct password
text_password = driver.find_element(By.ID,"input-password")
text_password.send_keys("Password!")
print(text_password.get_attribute("Value"))
assert text_password is not None
assert text_password.get_attribute("value") == "Password!"

#Step 5: Click Login button
button_login2 = wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@type = 'submit' and @value = 'Login']")))
button_login2.click()

text_myAccount = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"a[href*='account/edit']")))

        # Scenario 4: Forgotten password - Valid

#Step 1: Enter the website
driver = webdriver.Safari()
driver.get("https://opencart.abstracta.us/index.php?route=common/home")

wait = WebDriverWait(driver, 10)

#Step 2: Click on My Account, and then Register
button_myAccount = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"a[title='My Account']")))
button_myAccount.click()

button_login1 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"a[href*='account/login']")))
button_login1.click()

element = wait.until(EC.presence_of_element_located((By.ID,"account-login")))

#Step 3: Click Forgotten button
button_forgotten = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"a[href*='account/forgotten']")))
button_forgotten.click()

forgotten_page = wait.until(EC.presence_of_element_located((By.ID,"account-forgotten")))

#Step 4: Put an Email
text_email = driver.find_element(By.XPATH,"//input[@type = 'text' and @name = 'email' and @placeholder='E-Mail Address' and @id='input-email']")
text_email.send_keys("emily1@test.com")
print(text_email.get_attribute("Value"))
assert text_email is not None
assert text_email.get_attribute("value") == "emily1@test.com"

#Step 5: Click Continue button
button_continue = wait.until(EC.presence_of_element_located((By.XPATH,"//input[@type = 'submit' and @value = 'Continue']")))
button_continue.click()

confirmation_page = wait.until(EC.presence_of_element_located((By.CLASS_NAME,"alert-success")))

        #   Scenario 5: Forgotten Password - Incorrect Email 

#Step 1: Enter the website
driver = webdriver.Safari()
driver.get("https://opencart.abstracta.us/index.php?route=common/home")

wait = WebDriverWait(driver, 10)

#Step 2: Click on My Account, and then Register
button_myAccount = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"a[title='My Account']")))
button_myAccount.click()

button_login1 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"a[href*='account/login']")))
button_login1.click()

element = wait.until(EC.presence_of_element_located((By.ID,"account-login")))

#Step 3: Click Forgotten button
button_forgotten = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"a[href*='account/forgotten']")))
button_forgotten.click()

forgotten_page = wait.until(EC.presence_of_element_located((By.ID,"account-forgotten")))

#Step 4: Put an Email
text_email = driver.find_element(By.XPATH,"//input[@type = 'text' and @name = 'email' and @placeholder='E-Mail Address' and @id='input-email']")
text_email.send_keys("1233254245435563.f@example.com")
print(text_email.get_attribute("Value"))
assert text_email is not None
assert text_email.get_attribute("value") == "1233254245435563.f@example.com"

#Step 5: Click Continue button
button_continue = wait.until(EC.presence_of_element_located((By.XPATH,"//input[@type = 'submit' and @value = 'Continue']")))
button_continue.click()


time.sleep(10)
driver.quit()