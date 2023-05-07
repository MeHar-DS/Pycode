import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class DemoRadio:
    def demo_radio_button(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.sugarcrm.com/au/request-demo/")
        driver.maximize_window()
        time.sleep(2)
        driver.find_element(By.ID, "doi0").click()
        print(driver.find_element(By.ID,"doi0").is_selected())
        time.sleep(4)


demoradio =DemoRadio()
demoradio.demo_radio_button()