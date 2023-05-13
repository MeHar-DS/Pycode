import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class demoScreenshot:
    def demo_screen_capture(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        button = driver.find_element(By.XPATH, "//button[@id = 'login-continue-btn']")
        print(button.get_attribute("id"))
        button.click()
        time.sleep(3)
        button.screenshot(".\\test.png")
        time.sleep(2)
        driver.get_screenshot_as_file("C:\\Mervin\\testscreenshots\\error.jpg")
        driver.save_screenshot("C:\\Mervin\\testscreenshots\\error1.png")


objscr = demoScreenshot()
objscr.demo_screen_capture()