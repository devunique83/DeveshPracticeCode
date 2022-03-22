from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


class DemoSliders:
    def demo_slider(self):
        driver = webdriver.Chrome()
        driver.get("https://www.snapdeal.com/search?keyword=shoes&santizedKeyword=&catId=&categoryId=0&suggested=false&vertical=&noOfResults=20&searchState=&clickSrc=go_header&lastKeyword=&prodCatId=&changeBackToAll=false&foundInAll=false&categoryIdSearched=&cityPageUrl=&categoryUrl=&url=&utmContent=&dealDetail=&sort=rlvncy&q=Price%3A94%2C7276%7C")
        driver.maximize_window()
        action = ActionChains(driver)
        left = driver.find_element(By.XPATH,"//a[contains(@class,'left-handle')]")
        right = driver.find_element(By.XPATH,"//a[contains(@class,'right-handle')]")
        action.drag_and_drop_by_offset(left,50,0).perform()
        time.sleep(3)
        action.click_and_hold(left).pause(1).move_by_offset(50,0).pause(1).release().perform()
        time.sleep(3)
        action.move_to_element(left).pause(1).click_and_hold(left).pause(1).move_by_offset(50,0).pause(1).release().perform()
        time.sleep(3)
        action.drag_and_drop_by_offset(right,-40,0).perform()
        time.sleep(3)
        driver.quit()

obj=DemoSliders()
obj.demo_slider()