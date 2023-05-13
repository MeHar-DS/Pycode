import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait

class demoIframe:
    def demo_iframe(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_iframe_frameborder_css")

        # Switch with iframe locator

        driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@id='iframeResult']"))

        # switch with id

        driver.switch_to.frame("iframeResult")

        # switch with name

        driver.switch_to.frame("iframeResult")

        # Switch by iframe index
        driver.switch_to.frame(0)  # We have used index 0 since there are no id or other identifier
        driver.find_element(By.XPATH, "//a[contain(text(),'Tutorials ']").click()
        time.sleep(3)


diframe = demoIframe()
diframe.demo_iframe()