from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys





#added comment

driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")
driver.maximize_window()
ac = ActionChains(driver)
