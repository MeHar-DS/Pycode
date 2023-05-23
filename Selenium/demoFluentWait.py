import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager


class demoFluentWait:
    def fluent(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())