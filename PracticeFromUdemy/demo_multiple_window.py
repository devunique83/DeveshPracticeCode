import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path=r"C:\Users\deveshsharma\Desktop\To Transfer\From E\PracticeCode\PythonSelenium\BrowserDrivers\chromedriver.exe")
driver.get("http://the-internet.herokuapp.com/windows")
driver.maximize_window()

parent_handle = driver.current_window_handle
title1=driver.title
print(title1)

driver.find_element(By.XPATH,"//a[normalize-space()='Click Here']").click()
time.sleep(2)

handles = driver.window_handles
print(len(handles))

for handle in handles:
    if handle != parent_handle:
        driver.switch_to.window(handle)
title2= driver.title
print(title2)
driver.close()
time.sleep(2)

driver.switch_to.window(parent_handle)
title3= driver.title
print(title3)

assert title1 == title3

driver.quit()




