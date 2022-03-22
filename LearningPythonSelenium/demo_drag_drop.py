from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


class DemoDragDrop:
    def demo_drag_drop(self):
        driver = webdriver.Chrome()
        driver.get("https://www.globalsqa.com/demo-site/draganddrop/")
        driver.maximize_window()
        action = ActionChains(driver)
        driver.switch_to.frame("google_esf")
        time.sleep(2)
        ele1= driver.find_element(By.XPATH,"//img[@alt='Planning the ascent']")
        ele2=driver.find_element(By.ID,"trash")
        action.drag_and_drop(ele1,ele2).perform()
        time.sleep(4)
        driver.quit()

obj = DemoDragDrop()
obj.demo_drag_drop()
