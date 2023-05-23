import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options

class demoRightClick:
    def rightclick(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://demo.guru99.com/test/simple_context_menu.html")
        driver.maximize_window()
        #Right click
        achains =  ActionChains(driver)
        right_click = driver.find_element(By.XPATH, "//a[@span = 'context-menu-one btn btn-neutral']")
        copyelem = driver.find_element(By.XPATH, "//span[normalize-space()='Copy']")
        achains.context_click(right_click).perform()
        time.sleep(3)
        copyelem.click()
        time.sleep(3)

        # Double Click
        achains2 = ActionChains(driver)
        elem2 = driver.find_element(By.XPATH, "//button[normalize-space()='Double-Click Me To See Alert']")
        achains2.double_click(elem2).perform()
        time.sleep(3)


drtobj = demoRightClick()
drtobj.rightclick()

