from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.maximize_window()
driver.find_element_by_id("kw").send_keys("Python")
time.sleep(3)
driver.find_element_by_id("su").click()
driver.quit()
