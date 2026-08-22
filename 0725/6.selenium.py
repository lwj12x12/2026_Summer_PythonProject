from idlelib import search

from selenium import webdriver
import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.google.com/")
time.sleep(1)
search = driver.find_element(By.CLASS_NAME,'gLFyf')

search.send_keys('Hello')
time.sleep(5)

search.send_keys(Keys.ENTER)

driver.save_screenshot('test1.png')
time.sleep(2)

driver.quit()