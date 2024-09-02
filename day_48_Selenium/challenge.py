from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# Keep chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Create and configure the chrome webdriver
driver = webdriver.Chrome(options=chrome_options)

# Navigate to the secure-retreat-92358.herokuapp.com/ form page
driver.get("https://secure-retreat-92358.herokuapp.com/")


# Fill in first and last names:
first_name = driver.find_element(By.NAME, value="fName")
last_name = driver.find_element(By.NAME, value="lName")
email = driver.find_element(By.NAME, value="email")



# Fill out the form
first_name.send_keys("Uri")
last_name.send_keys("Gakuru")
email.send_keys("urigakuru@gmail.com")


# Locate sign up button and click on it
submit = driver.find_element(By.CSS_SELECTOR, value="form button")
submit.click()










# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys


# # Keep browser open after program finishes
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("detach", True)

# # Create and configure chrome webdriver
# driver = webdriver.Chrome(options=chrome_options)

# # Navigate to the wikipedia main page
# driver.get("https://secure-retreat-92358.herokuapp.com/")

# # Fill in first and last names:
# first_name = driver.find_element(By.NAME, value="fName")
# last_name = driver.find_element(By.NAME, value="lName")
# email = driver.find_element(By.NAME, value="email")

# # Fill out the form
# first_name.send_keys("John")
# last_name.send_keys("Doe")
# email.send_keys("johndoe@example.com")

# # Locate the sign up button. Then click on it
# submit = driver.find_element(By.CSS_SELECTOR, value="form button")
# submit.click()