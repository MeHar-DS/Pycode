import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

class demoDragDrop:
    def draganddrop(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.globalsqa.com/demo-site/draganddrop/")
        driver.maximize_window()
        driver.switch_to.frame(driver.find_element(By.XPATH,"//div[@rel-title='Photo Manager']//iframe[@class='demo-frame lazyloaded']"))
        elem1 = driver.find_element(By.XPATH, "//img[@alt='The peaks of High Tatras']")
        elem2 = driver.find_element(By.XPATH, "//div[@id='trash']")
        #ActionChains(driver).drag_and_drop(elem1,elem2).perform()  # Method 1
        ActionChains(driver).drag_and_drop_by_offset(elem1,400,0).perform()
        time.sleep(3)

dd = demoDragDrop()
dd.draganddrop()

