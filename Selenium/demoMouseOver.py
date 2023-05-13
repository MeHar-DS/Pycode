import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class demoMouseOver:
    def mouseevents(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.yatra.com")
        driver.maximize_window()
        moreButton = driver.find_element(By.XPATH, "//span[@class= 'more-arr']")
        achains = ActionChains(driver)
        achains.move_to_element(moreButton).perform()
        time.sleep(3)

        driver.find_element(By.XPATH, "//a[@title = 'Xplore']").click()

dmouse = demoMouseOver()
dmouse.mouseevents()