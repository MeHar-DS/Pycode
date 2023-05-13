import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class demo_js_execution:
    def js_execution(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        #driver.get("https://training.rcvacademy.com")
        # using java script execution method
        driver.execute_script("window.open('https://training.rcvacademy.com', '_self');")   #_self parameter
        time.sleep(5)
        elem = driver.execute_script("return document.getElementsByTagName('p')[0];")
        driver.execute_script("argument[0].click();",elem)


dobj = demo_js_execution()
dobj.js_execution()