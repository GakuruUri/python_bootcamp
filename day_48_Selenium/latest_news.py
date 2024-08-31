from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)



driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

# driver.get("https://www.amazon.com/")


events = driver.find_element(By.XPATH, 
value='').text.splitlines()
 
dictionary = { i: {'time': events[i], 'name': events[i+1]} for i in range(0, len(events), 2)}
 
print(dictionary)
 
driver.quit()



//*[@id="content"]/div/section/div[2]/div[2]/div/ul