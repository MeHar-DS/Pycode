from selenium import webdriver
#from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

#options = Options() #works
#options.add_argument("start-maximized")#To launch a maximised browser #works
#options.add_experimental_option("detach", True) # This helps sustain the browser, otherwise it immediately closes#works
#driver = webdriver.Chrome(executable_path="C:\\Mervin\\Selenium\\browserdrivers\\chromedriver_win32\\chromedriver.exe",options=options)#works
#driver = webdriver.Chrome(executable_path="C:\\Mervin\\Selenium\\browserdrivers\\chromedriver_win32\\chromedriver.exe")
#driver = webdriver.Chrome(service= Service(ChromeDriverManager().install())) #This works
driver = webdriver.Chrome(ChromeDriverManager().install()) #since the ChromeDriverManager is importedthisissufficient
driver.get("https://www.google.com")
driver.maximize_window()
print(driver.title)
driver.close()

