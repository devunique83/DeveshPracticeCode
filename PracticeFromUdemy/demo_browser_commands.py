import time
from selenium import webdriver



#driver = webdriver.Chrome(executable_path=r"C:\Users\deveshsharma\Desktop\To Transfer\From E\PracticeCode\PythonSelenium\BrowserDrivers\chromedriver.exe")
driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
print(driver.current_url)
print(driver.title)
driver.get("https://rahulshettyacademy.com/")
print(driver.current_url)
print(driver.title)
driver.back()
print(driver.current_url)
print(driver.title)
driver.minimize_window()
time.sleep(3)
driver.maximize_window()
driver.forward()
print(driver.current_url)
print(driver.title)
driver.quit()
