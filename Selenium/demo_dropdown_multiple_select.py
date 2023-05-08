import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

class DemoDropdownMultiSelect:
    def multi_select(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.seleniumeasy.com/test/basic-select-dropdown-demo.html")
        dd = driver.find_element(By.NAME,"")
        dd_multi = Select(dd)
        dd.select_by_index(1)
        dd.select_by_value("val2")
        dd.select_by_visible_text("val3")

        time.sleep(2)

        dd.deselect_by_index(1)
        dd.deselect_by_value("val2")
        dd.deselect_by_visible_text("val3")
        dd.deselect_all()

