import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

class DemoCheckbox:
    def demo_checkbox(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.salesforce.com/in/form/signup/freetrial-sales/?d=topnav2-btn-ft")
        dropdown = driver.find_element(By.NAME,"UserTitle")
        dd = Select(dropdown)
        dd.select_by_index(1)
        time.sleep(2)
        dd.select_by_value("Customer_Service_Manager_AP")
        time.sleep(2)
        dd.select_by_visible_text("Marketing / PR Manager")
        time.sleep(2)


obj = DemoCheckbox()
obj.demo_checkbox()