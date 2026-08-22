import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
url = 'https://www.nike.com/tw/w/new-womens-3n82yz5e1x6'
driver.get(url)
driver.maximize_window()
time.sleep(3)

titles = driver.find_elements(By.CLASS_NAME, 'product-card__title')
# print(titles)
for title in titles:
    print(title)


time.sleep(2)

driver.quit()