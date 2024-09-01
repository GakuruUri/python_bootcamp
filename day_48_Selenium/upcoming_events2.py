from selenium import webdriver
from selenium.webdriver.common.by import By

#Keep browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https:www.python.org/")

bug_link = driver.find_element(By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul')
tier_1 = driver.find_elements(By.CLASS_NAME, value='tier-1')


# Challenge: print the event dates from python.org
event_times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")

upcoming_events = {}

for n in range(len(event_times)):
    upcoming_events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text,
    }

    print(upcoming_events)

    driver.quit()