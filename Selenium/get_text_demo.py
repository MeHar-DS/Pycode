import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class DemoGetText:
    def demo_get_text_methods(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://secure.yatra.com/")
        driver.maximize_window()
        time.sleep(2)
        #driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        #driver.get("https://training.rcvacademy.com")
        #driver.find_element(By.ID, "login-input").send_keys('test@test.com')
        #driver.find_element(By.NAME, "login-input").send_keys('test@test.com')
        t = driver.find_element(By.XPATH, "//span[contains(text(),'Popular domestic Flight Routes')]").text
        t2 = driver.find_element(By.LINK_TEXT,"Yatra for Business").text
        #driver.find_element(By.CSS_SELECTOR,"#login-input").send_keys('test@test.com')
        #print(t)
        print(t2)


demoBrowser = DemoGetText()
demoBrowser.demo_get_text_methods()



