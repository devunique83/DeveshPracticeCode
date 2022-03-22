from selenium import webdriver
driver = webdriver.Chrome(executable_path="E:\\PracticeCode\\PythonSelenium\\BrowserDrivers\\chromedriver.exe")

driver.get("https://www.amazon.in/")
title = driver.title
print(title)

#assert title != "Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in"

driver.maximize_window()


driver.quit()