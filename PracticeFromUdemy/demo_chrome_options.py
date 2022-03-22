import time
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--ignore-certificate-errors")

driver = webdriver.Chrome(executable_path=r"C:\Users\deveshsharma\Desktop\To Transfer\From E\PracticeCode\PythonSelenium\BrowserDrivers\chromedriver.exe",options=chrome_options)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
print(driver.title)
driver.quit()
