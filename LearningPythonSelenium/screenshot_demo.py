from selenium import webdriver
from selenium.webdriver.common.by import By



driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")
driver.maximize_window()
driver.get_screenshot_as_file("screen.png")
driver.get_screenshot_as_file("screen1.jpg")
driver.save_screenshot("test.png")
ele = driver.find_element(By.XPATH,"//a[normalize-space()='Forgotten password?']")
ele.screenshot("element.png")

#driver.get_screenshot_as_base64()
driver.quit()