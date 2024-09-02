from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Keep chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Create and configure the chrome webdriver
driver = webdriver.Chrome(options=chrome_options)

# Navigate to the cookie monster website.
driver.get("https://orteil.dashnet.org/cookieclicker/")


# Simulate 1000000 clicks on the cookie monster.

language = driver.find_element(By.ID, "English")
language.click()
clicker = driver.find_element(By.ID, value="bigCookie")
clicker.click()
