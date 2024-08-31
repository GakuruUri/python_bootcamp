from selenium import webdriver

# Keep chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)



driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://www.amazon.com/")
driver.get("https://www.amazon.com/Instant-Pot-Plus-60-Programmable/dp/B01NBKTPTS/ref=sr_1_1?crid=1RRP3RMZL6W22&dib=eyJ2IjoiMSJ9.JCyn2nZZp1sOG9u3pnBnuofZogJhhDwYTw2Z3fPl3jmY8ocHICNFU7vefeWm8f-kCAgl2CYp8xFRR3VKWmkHdgMumgJwQQmdl_yWUwJF-p-eHesKd-u191CE3glXhdyKMoaqHvcnONRQNS0CDE9pNTE92hyfCHVh9lfq428Gj0DjwKpWl7X7hy6TJfNLH-jNT-CTfJJ2a-G9Axm7ieh-k_8w-i1ITgLq1jS78w6YtoQ.Z17V1gAubv4vHyb0-bgM_GTQKz35PtXx2XuMQHNoKfE&dib_tag=se&keywords=Instant%2BPot%2BDuo%2BPlus%2B9-in-1%2BElectric%2BPressure&qid=1725079813&sprefix=instant%2Bpot%2Bduo%2Bplus%2B9-in-1%2Belectric%2Bpressure%2Caps%2C1010&sr=8-1&th=1")



# driver.close()
# driver.quit()