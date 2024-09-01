from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Keep chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


# Create and configure the chrome webdriver
driver = webdriver.Chrome(options=chrome_options)


# Navigate to the wikipedia main page
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# Hone in on anchor tag using CSS selectors
article_count = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
# article_count.click()
# print(article_count.text)



# Find elements by link text
all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# all_portals.click()


search = driver.find_element(By.NAME, value="search")


# Send keys to the search bar
search.send_keys("python", Keys.ENTER)
# search.send_keys(Keys.ENTER)


# driver.quit()

















# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# # Keep chrome browser open after program finishes
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("detach", True)

# # Create and configure the chrome webdriver
# driver = webdriver.Chrome(options=chrome_options)

# # Navigate to the wikipedia main page
# driver.get("https://en.wikipedia.org/wiki/Main_Page")


# # Find the search bar element (modify the selector as needed)
# try:
#     search_bar = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.ID, "searchInput"))  # Replace with actual ID
#     )
# except TimeoutException:
#     print("Search bar element not found!")
#     driver.quit()
#     exit(1)

# # Send keys to the search bar and press ENTER
# search_bar.send_keys("python", Keys.ENTER)

# # You can add further code to handle search results here

# driver.quit()

