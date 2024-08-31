from selenium import webdriver
from selenium.webdriver.common.by import By


# Keep browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https:/www.python.org/")


# Find the search bar element
events = driver.find_element(By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul').text.splitlines()

dict = {
    i: {'time': events[i],
    'name': events[i+1]}
    for i in range(0, len(events), 2)
}

print(dict)

driver.quit()