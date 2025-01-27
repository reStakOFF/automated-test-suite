from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://demo.opencart.com")
time.sleep(5)
    
driver.find_element(By.LINK_TEXT, "My Account").click()
time.sleep(5)
driver.find_element(By.LINK_TEXT, "My Account").click()
time.sleep(5)
driver.find_element(By.LINK_TEXT, "Login").click()
time.sleep(3)
driver.find_element(By.NAME, "email").send_keys("test@example.com")
time.sleep(3)
driver.find_element(By.NAME, "password").send_keys("123456")
time.sleep(3)
driver.find_element(By.NAME, "Login").click()
time.sleep(3)
assert "My Account" in driver.title