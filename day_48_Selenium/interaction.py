from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# Keep browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")


event = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/a[1]')
# print(event.text)
search = driver.find_element(By.NAME, value="search")
search.send_keys("python", Keys.ENTER)

driver.quit()