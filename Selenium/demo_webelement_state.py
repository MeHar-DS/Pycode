import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class DemoElementState:
    def demo_enable_disable(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        #ChromeOptions options = new ChromeOptions();
        #options.addArguments("--disable-notifications");
        #driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(),options)
        driver.get("http://training.openspan.com/login")
        driver.maximize_window()
        demo_state = driver.find_element(By.XPATH, "//input[@id='login_button']").is_enabled()
        print(demo_state)
        driver.find_element(By.XPATH, "//input[@id='user_name']").send_keys("testing")
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@id='user_pass']").send_keys("testing")
        time.sleep(2)
        state2 = driver.find_element(By.XPATH, "//input[@id='login_button']").is_enabled()
        print(state2)


demoState = DemoElementState()
demoState.demo_enable_disable()



