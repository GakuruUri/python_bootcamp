from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Optional keep the browser open(Helps diagonise issue if browser crushed.
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)