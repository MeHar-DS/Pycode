import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class DemoCheckboxes:
    def demo_checkboxes(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.sugarcrm.com/au/request-demo/")
        driver.maximize_window()
        driver.find_element(By.ID, "interest-market-c0").click()
        time.sleep(2)

checkbox = DemoCheckboxes()
checkbox.demo_checkboxes()



