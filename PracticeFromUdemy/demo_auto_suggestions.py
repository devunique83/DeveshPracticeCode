import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=r"C:\Users\deveshsharma\Desktop\To Transfer\From E\PracticeCode\PythonSelenium\BrowserDrivers\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.maximize_window()

driver.find_element(By.XPATH,"//input[@id='autosuggest']").send_keys("new")
time.sleep(2)
countries = driver.find_elements(By.XPATH,"//ul/li[@class='ui-menu-item']/a")
for country in countries:
    if country.text == 'New Zealand':
        country.click()
        time.sleep(2)
        break
#print(driver.find_element(By.XPATH,"//input[@id='autosuggest']").text)
# the updated value New Zealand would not show as selenium reads the value when DOm is loaded and we have updated the
#value after Dom loaded, hence selenium can not read it. hence
print(driver.find_element(By.XPATH,"//input[@id='autosuggest']").get_attribute('value'))


driver.quit()