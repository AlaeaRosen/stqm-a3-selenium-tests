import selenium 
from selenium import webdriver 
import time 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# TEST CASE 2 - USER REGISTRATION FROM HOME PAGE
# Scenario 1:

#Step 1: Enter the website
driver = webdriver.Safari()
driver.get("https://opencart.abstracta.us/index.php?route=common/home")
wait = WebDriverWait(driver, 5) 

#Step 2: Click on My Account, and then Register
button_myAccount = driver.find_element(By.CLASS_NAME,"dropdown")
button_myAccount.click()

button_register  = driver.find_element(By.LINK_TEXT,"Register")
button_register.click()

wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.ID,"input-firstname")))

#Step 3: Add First Name
text_firstname = driver.find_element(By.ID,"input-firstname")
text_firstname.send_keys("Emily")
print(text_firstname.get_attribute("Value"))
assert text_firstname is not None
assert text_firstname.get_attribute("value") == "Emily"

#Step 4: Add Last Name
text_lastname = driver.find_element(By.ID,"input-lastname")
text_lastname.send_keys("Fons")
print(text_lastname.get_attribute("Value"))
assert text_lastname is not None
assert text_lastname.get_attribute("value") == "Fons"

#Step 5: Add Email
text_email = driver.find_element(By.ID,"input-email")
text_email.send_keys("emily.fons@gmail.com")
print(text_email.get_attribute("Value"))
assert text_email is not None
assert text_email.get_attribute("value") == "emily.fons@gmail.com"

#Step 6: Add Telephone
text_telephone = driver.find_element(By.ID,"input-telephone")
text_telephone.send_keys("0400100100")
print(text_telephone.get_attribute("Value"))
assert text_telephone is not None
assert text_telephone.get_attribute("value") == "0400100100"

#Step 7: Add Password
text_password = driver.find_element(By.ID,"input-password")
text_password.send_keys("Password!12")
print(text_password.get_attribute("Value"))
assert text_password is not None
assert text_password.get_attribute("value") == "Password!12"

#Step 8: Add Password Confirm
text_confirm = driver.find_element(By.ID,"input-confirm")
text_confirm.send_keys("Password!12")
print(text_confirm.get_attribute("Value"))
assert text_confirm is not None
assert text_confirm.get_attribute("value") == "Password!12"

#Step 9: Select Yes to Subscribe Newsletter
newsletter = driver.find_element(By.CLASS_NAME,"radio-inline")
subscribe_radio = driver.find_element(By.XPATH,"//input[@type = 'radio' and @name = 'newsletter' and @value = '1']")
subscribe_radio.click()



time.sleep(10)
