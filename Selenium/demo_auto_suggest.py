import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

class DemoAutoSuggest:
    def auto_suggest(self):
        options = Options()
        options.add_argument("--disable-notifications")
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
        driver.get("https://www.yatra.com")
        depart_from = driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_city']")
        depart_from.click()
        depart_from.send_keys("New Delhi")  # Types the characters required
        time.sleep(2)
        depart_from.send_keys(Keys.ENTER)   # Replicates the action of hitting enter key
        time.sleep(4)
        going_to = driver.find_element(By.XPATH, "//input[@id='BE_flight_arrival_city']")
        going_to.send_keys("New")
        time.sleep(3)
        list_results = driver.find_elements(By.XPATH, "//div[@class = 'viewport']//div[1]/li")
        print(len(list_results))
        for results in list_results:
            #print(results.text)
            if "New York (JFK)" in results.text:
                results.click()
                time.sleep(5)
                break
        wait = WebDriverWait(driver, timeout=10)
        origin = driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_date']")
        wait.until(element_to_be_clickable(origin))
        time.sleep(1)
        origin.click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//td[@id='18/05/2023']").click()
        time.sleep(3)



sauto = DemoAutoSuggest()
sauto.auto_suggest()
