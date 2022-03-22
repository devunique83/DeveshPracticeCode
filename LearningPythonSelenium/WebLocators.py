from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import  ActionChains
from selenium.webdriver import DesiredCapabilities

import time


driver= webdriver.Chrome(executable_path="E:\\PracticeCode\\PythonSelenium\\BrowserDrivers\\chromedriver.exe")
driver.get("http://localhost:5001/")
driver.maximize_window()
#file_bug = driver.find_element(By.ID,"enter_bug")
#file_bug = driver.find_element(By.CLASS_NAME,"bz_common_actions")
#file_bug=driver.find_element(By.LINK_TEXT,"File a Bug")
#file_bug=driver.find_element(By.PARTIAL_LINK_TEXT,"Fil")
# file_bug=driver.find_element_by_id("enter_bug")
# print(file_bug.text)
# file_bug.click()
# search=driver.find_elements_by_xpath("//form/div/input")
# search[0].send_keys("123")
# search[1].click()
# time.sleep(2)
# print(driver.find_element_by_id("error_msg").text)
# print("before cookies")
# cookies=driver.get_cookies()
# print(cookies)
# for i,j in enumerate(cookies):
#     print("loop")
#     print(i,j)
# for i in driver.window_handles:
#     print(i)
driver.switch_to_frame()
time.sleep(4)
driver.close()

