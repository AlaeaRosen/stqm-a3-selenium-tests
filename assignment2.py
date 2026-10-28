import selenium 
from selenium import webdriver 
import time 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Safari()
driver.get("https://opencart.abstracta.us/index.php?route=common/home")
wait = WebDriverWait(driver, 5)

# TEST CASE 2 - USER REGISTRATION FROM HOME PAGE
# Scenario 1: 

#Step 1
button_myAccount = driver.find_element(By.CLASS_NAME,"dropdown")
button_myAccount.click()

button_register  = driver.find_element(By.LINK_TEXT,"Register")
button_register.click()

wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.ID,"input-firstname")))

#Step 2
text_firstname = driver.find_element(By.ID,"input-firstname")
text_firstname.send_keys("Emily")
print(text_firstname.get_attribute("Value"))
assert text_firstname is not None
assert text_firstname.get_attribute("value") == "Emily"

#Step 3
text_firstname = driver.find_element(By.ID,"input-lastname")
text_firstname.send_keys("Fons")
print(text_firstname.get_attribute("Value"))
assert text_firstname is not None
assert text_firstname.get_attribute("value") == "Fons"

time.sleep(10)
