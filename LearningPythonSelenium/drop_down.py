from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.facebook.com/")
driver.maximize_window()
driver.find_element(By.XPATH,"//a[text()='Create New Account']").click()
select = Select(driver.find_element(By.CSS_SELECTOR,"#day"))
print(select.is_multiple)
select.select_by_index(4)
ele = driver.find_element(By.CSS_SELECTOR,"#month")

all_options = ele.find_elements(By.TAG_NAME,'option')
for option in all_options:
    print(option.text)
#    print(option.get_attribute('value'))
element=driver.find_element(By.XPATH,"//label[normalize-space()='Male']").click()
if element.is_selected():
    print("Y")
else:
    print("N")

time.sleep(5)


driver.quit()

