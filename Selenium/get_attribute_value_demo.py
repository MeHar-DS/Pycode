import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class DemoGetAttributeValue:
    def demo_get_attribute_value(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        #ChromeOptions options = new ChromeOptions();
        #options.addArguments("--disable-notifications");
        #driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(),options)
        driver.get("https://secure.yatra.com/")
        driver.maximize_window()
        time.sleep(2)
        #driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        #driver.get("https://training.rcvacademy.com")
        #driver.find_element(By.ID, "login-input").send_keys('test@test.com')
        #driver.find_element(By.NAME, "login-input").send_keys('test@test.com')
        t = driver.find_element(By.XPATH, "//input[@id='BE_flight_flsearch_btn']").get_attribute("value")
        #driver.find_element(By.CSS_SELECTOR,"#login-input").send_keys('test@test.com')
        print(t)


demoBrowser = DemoGetAttributeValue()
demoBrowser.demo_get_attribute_value()



