import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

class demoSlider:
    def slide(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.snapdeal.com/products/mobiles-mobile-phones?sort=plrty")
        driver.maximize_window()
        elem1 = driver.find_element(By.XPATH, "//a[contains(@class,'left-handle')]")
        elem2 = driver.find_element(By.XPATH, "//a[contains(@class,'right-handle')]")
        #achains = ActionChains(driver).drag_and_drop_by_offset(elem1, 60, 0).perform()   # Method1
        #ActionChains(driver).click_and_hold(elem1).pause(2).move_by_offset(50,0).release().perform()  # Method2
        #ActionChains(driver).move_to_element(elem1).pause(1).click_and_hold(elem1).move_by_offset(80,0).release().perform()  # Method3

        #Move elem2 in left direction
        ActionChains(driver).drag_and_drop_by_offset(elem1,-70).perform()   #Method1
        time.sleep(3)



        time.sleep(3)



ds =demoSlider()
ds.slide()