import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


class demoExplicit:
    def explicit_wait_demo(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.yatra.com")
        driver.implicitly_wait(20)
        wait = WebDriverWait(driver, timeout=20)

        depart_from = driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_city']")
        wait.until(ec.element_to_be_clickable(depart_from)).click()
        # depart_from.click()
        depart_from.send_keys("New Delhi")  # Types the characters required
        depart_from.send_keys(Keys.ENTER)  # Replicates the action of hitting enter key
        time.sleep(2)

        #wait.until(element_to_be_clickable(driver.find_element(By.XPATH, "//input[@id='BE_flight_arrival_city']"))).click()
        going_to = driver.find_element(By.XPATH, "//input[@id='BE_flight_arrival_city']")
        wait.until(ec.element_to_be_clickable(going_to)).click()
        going_to.send_keys("New")
        time.sleep(3)
        wait.until(ec.element_to_be_clickable(driver.find_element(By.XPATH, "//div[@class = 'viewport']//div[1]/li")))
        list_results = driver.find_elements(By.XPATH, "//div[@class = 'viewport']//div[1]/li")
        print(len(list_results))
        for results in list_results:
            print(results.text)
            if "New York (JFK)" in results.text:
                results.click()
                time.sleep(3)
                break


        el = driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_date']")
        wait.until(ec.element_to_be_clickable(el)).click()
        # driver.execute_script("arguments[0].click();",el)
        time.sleep(3)

        # # Dynamic date entry

        # Wait with Expected Conditions syntax with object found using By as show below
        all_dates = wait.until(ec.element_to_be_clickable((By.XPATH, "//div[@id = 'monthWrapper']//tbody//td[@class!= 'inActiveTD weekend' or @class!= 'inActiveTD']")))\
            .find_elements(By.XPATH, "//div[@id = 'monthWrapper']//tbody//td[@class!= 'inActiveTD weekend' or @class!= 'inActiveTD']")


        # Wait with expected Conditions syntax with element name stored as variable directly as shown below

        for date in all_dates:
            if date.get_attribute('data-date') == "30/05/2023":
                date.click()
                time.sleep(3)
                break
        driver.find_element(By.XPATH, "//input[@id ='BE_flight_flsearch_btn']").click()


dexp = demoExplicit()
dexp.explicit_wait_demo()

