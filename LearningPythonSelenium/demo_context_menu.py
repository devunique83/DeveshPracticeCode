from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time



class DemoContextMenu:
    def demo_clicks(self):
        driver = webdriver.Chrome()
        driver.get("https://demo.guru99.com/test/simple_context_menu.html")
        driver.maximize_window()
        action = ActionChains(driver)
        action.context_click(driver.find_element(By.XPATH,"//span[@class='context-menu-one btn btn-neutral']")).perform()
        time.sleep(4)
        driver.find_element(By.XPATH,"//span[normalize-space()='Copy']").click()
        time.sleep(2)
        alert=driver.switch_to.alert
        print(alert.text)
        alert.accept()
        time.sleep(2)
        action.double_click(driver.find_element(By.XPATH,"//button[normalize-space()='Double-Click Me To See Alert']")).perform()
        time.sleep(2)
        alert1=driver.switch_to.alert
        print(alert.text)
        alert1.accept()
        time.sleep(2)
        driver.quit()

obj = DemoContextMenu()
obj.demo_clicks()