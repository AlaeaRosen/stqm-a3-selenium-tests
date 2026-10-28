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
wait = WebDriverWait(driver, 5) 

#Step 2: Click on My Account, and then Register
button_myAccount = driver.find_element(By.CLASS_NAME,"dropdown")
button_myAccount.click()

button_register  = driver.find_element(By.LINK_TEXT,"Login")
button_register.click()

wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.ID,"input-email")))

#Step 3: Put a correct Email
text_email = driver.find_element(By.ID,"input-email")
text_email.send_keys("emily.fons@test.com")
print(text_email.get_attribute("Value"))
assert text_email is not None
assert text_email.get_attribute("value") == "emily.fons@test.com"

#Step 3: Put a correct password
text_email = driver.find_element(By.ID,"input-email")
text_email.send_keys("emily.fons@test.com")
print(text_email.get_attribute("Value"))
assert text_email is not None
assert text_email.get_attribute("value") == "emily.fons@test.com"

time.sleep(10)
driver.quit()