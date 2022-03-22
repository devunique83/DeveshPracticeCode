from selenium import webdriver
import time
from selenium.webdriver.common.by import By


driver= webdriver.Chrome()
driver.get("https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_alert")
driver.maximize_window()
print(driver.title)
time.sleep(2)
driver.switch_to.frame("iframeResult")
driver.find_element(By.XPATH,"//button[normalize-space()='Try it']").click()
time.sleep(2)
alert = driver.switch_to.alert
print(alert.text)
alert.accept()
time.sleep(2)
driver.quit()