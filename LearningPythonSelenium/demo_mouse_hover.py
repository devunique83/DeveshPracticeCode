from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import  ActionChains
import time


class DemoMouseHover:
    def demo_mouse_hover(self):
        driver = webdriver.Chrome()
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        time.sleep(5)
        action = ActionChains(driver)
        more_ele=driver.find_element(By.XPATH,"//a[contains(text(),'My Account')]")
        action.move_to_element(more_ele).perform()
        time.sleep(5)
        (driver.find_element(By.XPATH,"//a[@id='SignUpBtn']")).click()
        time.sleep(5)
        print(driver.title)
        driver.quit()

obj=DemoMouseHover()
obj.demo_mouse_hover()

