from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("http://google.com")
driver.find_element_by_name("q").send_keys("Hongik University")
driver.find_element_by_name("btnK").click()
driver.maximize_window()
driver.refresh()
time.sleep(5)
driver.quit()
print("Test Completed Successfully.")
