import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class DemoSeleniumLearning:
    def demo_browser_methods(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        #driver.get("https://secure.yatra.com/")
        #driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.get("https://training.rcvacademy.com")
        print(driver.current_url)
        print(driver.title)
        driver.maximize_window()
        driver.fullscreen_window()
        driver.refresh()
        driver.find_element(By.LINK_TEXT, "ALL COURSES").click()
        time.sleep(3)
        driver.back()
        time.sleep(3)
        driver.forward()
        time.sleep(3)
        driver.minimize_window()
        time.sleep(2)
        driver.quit()
        #driver.find_element(By.ID, "login-input").send_keys('test@test.com')
        #driver.find_element(By.NAME, "login-input").send_keys('test@test.com')
        #driver.find_element(By.XPATH, "//input[@id='login-input']").send_keys('test@test.com')
        #driver.find_element(By.CSS_SELECTOR,"#login-input").send_keys('test@test.com')
        # l = driver.find_elements(By.TAG_NAME,"a")


demoBrowser = DemoSeleniumLearning()
demoBrowser.demo_browser_methods()



