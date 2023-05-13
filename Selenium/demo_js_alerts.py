import time
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options

class demoJsPopUp:
    def js_popup(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_prompt")
        driver.switch_to.frame(By.XPATH, "//iframe[@id = 'iframeResult']")

        #Accept Alert

        driver.find_element(By.XPATH, "//button[contains(text(),'Try')]").click()
        time.sleep(2)
        driver.switch_to.alert.accept()   # This is the Ok button click on popup
        time.sleep(2)

        # Switch to and then Dismiss Alert
        driver.find_element(By.XPATH, "//button[contains(text(),'Try')]").click()
        time.sleep(2)
        driver.switch_to.alert.dismiss()   # This is the cancel button click on popup
        time.sleep(2)

        #Switch to and Sendkeys and Accept
        driver.find_element(By.XPATH, "//button[contains(text(),'Try')]").click()
        time.sleep(2)
        print(driver.switch_to.alert.text)
        driver.switch_to.alert.send_keys("MERVIN")   # This is the entering of the text on the popup prompt
        driver.switch_to.alert.accept()  # This is the Ok button press on popup
        #Alert(driver).accept()   # Similar to Accept command above
        time.sleep(2)


jsobj = demoJsPopUp()
jsobj.js_popup()