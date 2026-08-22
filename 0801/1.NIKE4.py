import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
url = 'https://www.nike.com/tw/w/sale-3yaep'
driver.get(url)
driver.maximize_window()

count = 0
while True:
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight - 1500)")
    try:
        WebDriverWait(driver,5).until(
            EC.invisibility_of_element_located((By.CLASS_NAME,'loader-bar'))
        )
    except Exception as e:
        print(e)
    products = driver.find_elements(By.CLASS_NAME, 'product-card')
    if count == len(products):
        break
    count = len(products)
for product in products:
    titles = product.find_element(By.CLASS_NAME, 'product-card__titles').text
    print(titles)
    # driver.execute_script("window.scrollTo(0,3000)") #滑動畫面
driver.quit()