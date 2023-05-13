import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

class demomultiple:
    def demo_multi_window(self):
        #options = Options()  # Disabling popups code
        #options.add_argument('--disable_notifications')
        # options.page_load_strategy = 'normal'
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get('https://www.yatra.com')
        #driver.maximize_window()
        time.sleep(5)
        parent_handle = driver.current_window_handle
        print(parent_handle)
        time.sleep(5)
        driver.get_screenshot_as_file("C:\\Mervin\\testscreenshots\\error.jpg")
        wait = WebDriverWait(driver, timeout=10)
        domestic = driver.find_element(By.XPATH, "//img[contains(@alt,'Flat 12% OFF')]")
        wait.until(element_to_be_clickable(domestic))
        domestic.click()
        all_handles = driver.window_handles
        print(all_handles)
        for handle in all_handles:
            if handle != parent_handle:
                driver.switch_to.window(handle)
                driver.find_element(By.XPATH, "//a[@id = 'booking_engine_hotels']").click()
                time.sleep(3)
                driver.close()
                time.sleep(2)
                break

        driver.switch_to.window(parent_handle)


dobj = demomultiple()
dobj.demo_multi_window()