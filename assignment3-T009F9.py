import selenium 
from selenium import webdriver 
import time 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# TEST CASE 9 - POST A COMMENT/ REVIEW
        # Scenario 1: Valid

#Step 1: Enter the website
driver = webdriver.Safari()
driver.get("https://opencart.abstracta.us/index.php?route=common/home")

wait = WebDriverWait(driver, 10)
wait.until(lambda d: d.execute_script("return document.readyState") == "complete")

#Step 2: Click on MacBook product in the Featured section
button_product = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"a[href*='product_id=43']")))
button_product.click()

element = wait.until(EC.presence_of_element_located((By.ID,"tab-description")))

#Step 3: Click on Write a Review link
button_review = wait.until(EC.element_to_be_clickable((By.LINK_TEXT,"Write a review")))
button_review.click()

#Step 4: Enter Name
text_name= wait.until(EC.visibility_of_element_located((By.ID,"input-name")))
text_name.send_keys("Emily")
print(text_name.get_attribute("value"))
assert text_name.get_attribute("value") == "Emily"

#Step 5: Enter Review
text_review= driver.find_element(By.ID,"input-review")
text_review.send_keys("A really good product. The price is cheaper here compared to the other websites. I really recommend it!")
print(text_review.get_attribute("value"))
assert text_review.get_attribute("value") == "A really good product. The price is cheaper here compared to the other websites. I really recommend it!"

#Step 6: Select Rating radio button
radio_rating = driver.find_element(By.XPATH,"//input[@type = 'radio' and @name = 'rating' and @value = '5']")
radio_rating.click()
assert radio_rating.is_selected()

#Step 7: Click Continue button
button_continue = wait.until(EC.element_to_be_clickable((By.ID,"button-review")))
button_continue.click()

text_confirmation = wait.until(EC.visibility_of_element_located((By.CLASS_NAME,"alert-success")))
assert "Thank you for your review" in text_confirmation.text

time.sleep(10)
driver.quit()

        # Scenario 2: No name

#Step 1: Enter the website
driver = webdriver.Safari()
driver.get("https://opencart.abstracta.us/index.php?route=common/home")

wait = WebDriverWait(driver, 10)
wait.until(lambda d: d.execute_script("return document.readyState") == "complete")

#Step 2: Click on MacBook product in the Featured section
button_product = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"a[href*='product_id=43']")))
button_product.click()

element = wait.until(EC.presence_of_element_located((By.ID,"tab-description")))

#Step 3: Click on Write a Review link
button_review = wait.until(EC.element_to_be_clickable((By.LINK_TEXT,"Write a review")))
button_review.click()

#Step 4: Enter Review 
text_review= wait.until(EC.visibility_of_element_located((By.ID,"input-review")))
text_review.send_keys("A really good product. The price is cheaper here compared to the other websites. I really recommend it!")
print(text_review.get_attribute("value"))
assert text_review.get_attribute("value") == "A really good product. The price is cheaper here compared to the other websites. I really recommend it!"

#Step 5: Select Rating radio button
radio_rating = driver.find_element(By.XPATH,"//input[@type = 'radio' and @name = 'rating' and @value = '5']")
radio_rating.click()
assert radio_rating.is_selected()

#Step 6: Click Continue button
button_continue = wait.until(EC.element_to_be_clickable((By.ID,"button-review")))
button_continue.click()

warning = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,".alert-danger")))
assert "Review Name must be between 3 and 25 characters" in warning.text

time.sleep(10)
driver.quit()

        # Scenario 3: No Rating

#Step 1: Enter the website
driver = webdriver.Safari()
driver.get("https://opencart.abstracta.us/index.php?route=common/home")

wait = WebDriverWait(driver, 10)
wait.until(lambda d: d.execute_script("return document.readyState") == "complete")


#Step 2: Click on MacBook product in the Featured section
button_product = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"a[href*='product_id=43']")))
button_product.click()

element = wait.until(EC.presence_of_element_located((By.ID,"tab-description")))

#Step 3: Click on Write a Review link
button_review = wait.until(EC.element_to_be_clickable((By.LINK_TEXT,"Write a review")))
button_review.click()

#Step 4: Enter Name
text_name= wait.until(EC.visibility_of_element_located((By.ID,"input-name")))
text_name.send_keys("Emily")
print(text_name.get_attribute("value"))
assert text_name.get_attribute("value") == "Emily"

#Step 5: Enter Review
text_review= driver.find_element(By.ID,"input-review")
text_review.send_keys("A really good product. The price is cheaper here compared to the other websites. I really recommend it!")
print(text_review.get_attribute("value"))
assert text_review.get_attribute("value") == "A really good product. The price is cheaper here compared to the other websites. I really recommend it!"

#Step 6: Click Continue button
button_continue = wait.until(EC.element_to_be_clickable((By.ID,"button-review")))
button_continue.click()

warning = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,".alert-danger")))
assert "Please select a review rating" in warning.text

time.sleep(10)
driver.quit()

        # Scenario 4: Empty Review 

#Step 1: Enter the website
driver = webdriver.Safari()
driver.get("https://opencart.abstracta.us/index.php?route=common/home")

wait = WebDriverWait(driver, 10)
wait.until(lambda d: d.execute_script("return document.readyState") == "complete")

#Step 2: Click on MacBook product in the Featured section
button_product = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"a[href*='product_id=43']")))
button_product.click()

element = wait.until(EC.presence_of_element_located((By.ID,"tab-description")))

#Step 3: Click on Write a Review link
button_review = wait.until(EC.element_to_be_clickable((By.LINK_TEXT,"Write a review")))
button_review.click()

#Step 4: Enter Name
text_name= wait.until(EC.visibility_of_element_located((By.ID,"input-name")))
text_name.send_keys("Emily")
print(text_name.get_attribute("value"))
assert text_name.get_attribute("value") == "Emily"

#Step 5: Select Rating radio button
radio_rating = driver.find_element(By.XPATH,"//input[@type = 'radio' and @name = 'rating' and @value = '5']")
radio_rating.click()
assert radio_rating.is_selected()

#Step 6: Click Continue button
button_continue = wait.until(EC.element_to_be_clickable((By.ID,"button-review")))
button_continue.click()

warning = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,".alert-danger")))
assert "Review Text must be between 25 and 1000 characters" in warning.text

time.sleep(10)
driver.quit()

         # Scenario 5: Review too short

#Step 1: Enter the website
driver = webdriver.Safari()
driver.get("https://opencart.abstracta.us/index.php?route=common/home")

wait = WebDriverWait(driver, 10)
wait.until(lambda d: d.execute_script("return document.readyState") == "complete")

#Step 2: Click on MacBook product in the Featured section
button_product = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"a[href*='product_id=43']")))
button_product.click()

element = wait.until(EC.presence_of_element_located((By.ID,"tab-description")))

#Step 3: Click on Write a Review link
button_review = wait.until(EC.element_to_be_clickable((By.LINK_TEXT,"Write a review")))
button_review.click()

#Step 4: Enter Name
text_name= wait.until(EC.visibility_of_element_located((By.ID,"input-name")))
text_name.send_keys("Emily")
print(text_name.get_attribute("value"))
assert text_name.get_attribute("value") == "Emily"

#Step 5: Enter Review (exactly 24 characters)
text_review= driver.find_element(By.ID,"input-review")
text_review.send_keys("It was a bad bad product")
print(text_review.get_attribute("value"))
assert text_review.get_attribute("value") == "It was a bad bad product"

#Step 6: Select Rating radio button
radio_rating = driver.find_element(By.XPATH,"//input[@type = 'radio' and @name = 'rating' and @value = '1']")
radio_rating.click()
assert radio_rating.is_selected()


#Step 7: Click Continue button
button_continue = wait.until(EC.element_to_be_clickable((By.ID,"button-review")))
button_continue.click()

warning = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,".alert-danger")))
assert "Review Text must be between 25 and 1000 characters" in warning.text

time.sleep(10)
driver.quit()

       #Scenario 6: Name too short (exactly 2 characters)

#Step 1: Enter the website
driver = webdriver.Safari()
driver.get("https://opencart.abstracta.us/index.php?route=common/home")

wait = WebDriverWait(driver, 10)
wait.until(lambda d: d.execute_script("return document.readyState") == "complete")

#Step 2: Click on MacBook product in the Featured section
button_product = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"a[href*='product_id=43']")))
button_product.click()

element = wait.until(EC.presence_of_element_located((By.ID,"tab-description")))

#Step 3: Click on Write a Review link
button_review = wait.until(EC.element_to_be_clickable((By.LINK_TEXT,"Write a review")))
button_review.click()

#Step 4: Enter Name (exactly 2 characters)
text_name= wait.until(EC.visibility_of_element_located((By.ID,"input-name")))
text_name.send_keys("Em")
print(text_name.get_attribute("value"))
assert text_name.get_attribute("value") == "Em"

#Step 5: Enter Review
text_review= driver.find_element(By.ID,"input-review")
text_review.send_keys("A really good product. The price is cheaper here compared to the other websites. I really recommend it!")
print(text_review.get_attribute("value"))
assert text_review.get_attribute("value") == "A really good product. The price is cheaper here compared to the other websites. I really recommend it!"

#Step 6: Select Rating radio button
radio_rating = driver.find_element(By.XPATH,"//input[@type = 'radio' and @name = 'rating' and @value = '5']")
radio_rating.click()
assert radio_rating.is_selected()

#Step 7: Click Continue button
button_continue = wait.until(EC.element_to_be_clickable((By.ID,"button-review")))
button_continue.click()

warning = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,".alert-danger")))
assert "Review Name must be between 3 and 25 characters" in warning.text

time.sleep(10)
driver.quit()