
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

class DemoMultipleWindows:
    def demo_windows(self):
        driver=webdriver.Chrome()
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        parent=driver.current_window_handle
        print(driver.title)
        driver.find_element(By.XPATH,"//a[@title='Bahrain Packages']//img[@class='conta iner large-banner']").click()
        time.sleep(4)
        all_handles = driver.window_handles
        driver.switch_to.window(all_handles[1])
        print(driver.title)
        time.sleep(4)
        actions = ActionChains(driver)
        actions.context_click(driver.find_element(By.XPATH,"//a[@title='https://www.yatra.com']//i[@class='ico-newHeaderLogo']")).perform()
        time.sleep(4)
        driver.quit()
obj = DemoMultipleWindows()
obj.demo_windows()

