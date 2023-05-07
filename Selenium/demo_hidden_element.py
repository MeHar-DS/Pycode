import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class DemoElementState:
    def demo_element_visible(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.w3schools.com/howto/howto_js_toggle_hide_show.asp")
        elem = driver.find_element(By.XPATH, "//div[@id='myDIV']").is_displayed()
        print(elem)
        driver.find_element(By.XPATH, "//button[normalize-space()='Toggle Hide and Show']").click()
        elem2 = driver.find_element(By.XPATH, "//div[@id='myDIV']").is_displayed()
        print(elem2)

    def demo_is_displayed_yatra(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.yatra.com/hotels")
        driver.find_element(By.XPATH, "//label[@normalize-space()='Traveller and Hotel']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//div[@class = 'pax-limit clearfix w100 col-x-fluid fl']//span[@class='ddSpinnerPlus']").click()
        time.sleep(2)
        elem = driver.find_element(By.XPATH, "//select[@class='ageselect']").is_displayed()
        print(elem)


driverenable = DemoElementState()
driverenable.demo_is_displayed_yatra()