import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

class demoImplicit:
    def implicit(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.implicitly_wait(10)
        driver.get("https://login.salesforce.com/?locale=in")
        driver.find_element(By.ID, "username").send_keys("Mervin")
        driver.find_element(By.ID, "password").send_keys("Mervin")


dobj = demoImplicit()
dobj.implicit()