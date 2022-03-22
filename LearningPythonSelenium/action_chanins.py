from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
"""This is a Action Chains Demo file"

#added comment

driver = webdriver.Chrome() # to new driver object
driver.get("https://www.facebook.com/")
driver.maximize_window()
ac = ActionChains(driver)
