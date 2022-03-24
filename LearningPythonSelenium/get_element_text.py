from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")
driver.maximize_window()
# ele=driver.find_element(By.CSS_SELECTOR,"._8eso")
# print(ele.text)
#############################
"""get_attribute"""
# ele=driver.find_element(By.XPATH,"//a[normalize-space()='Forgotten password?']")
# print(ele.get_attribute('href'))
###############################
"""if element is enabled"""
ele=driver.find_element(By.CSS_SELECTOR,"#pass")
if ele.is_enabled():
    print("enabled")
if ele.is_displayed(): # for hidden element
    print("displayed")
if ele.is_selected(): #used for checkbox and radio button
    print("selected")
else:
    print("not selected")
print("script passed.")    
driver.quit()
