from selenium import  webdriver


class DemoIframe:
    def demo_iframe(self):
        driver= webdriver.Chrome()
        driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_iframe_frameborder_css")
        driver.maximize_window()
        driver.switch_to.frame("iframeResult")
        
