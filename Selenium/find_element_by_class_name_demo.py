import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class DemoFindElementByIDandName:
    def locate_by_id_demo(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.maximize_window()
        #driver.find_element(By.ID, "login-input").send_keys('test@test.com')
        #driver.find_element(By.NAME, "login-input").send_keys('test@test.com')
        #driver.find_element(By.XPATH, "//input[@id='login-input']").send_keys('test@test.com')
        #driver.find_element(By.CSS_SELECTOR,"#login-input").send_keys('test@test.com')
        #driver.find_element(By.LINK_TEXT,"Yatra for Business").click()
        #driver.find_element(By.PARTIAL_LINK_TEXT,"Yatra for").click()
        #driver.find_element(By.TAG_NAME,'input').send_keys('test@test.com')
        #driver.find_element(By.CLASS_NAME,"yt-sme-mobile-input required_field email-login-box").send_keys('test@test.com')
        driver.find_element(By.CLASS_NAME, "email-login-box").send_keys('test@test.com')
        time.sleep(3)


findbyid = DemoFindElementByIDandName()
findbyid.locate_by_id_demo()


