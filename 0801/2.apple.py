import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import openpyxl

wb = openpyxl.Workbook()
ws = wb.active

ws.append(['商品名稱', '價格', '商品連結'])

url = 'https://www.apple.com/tw/'
driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()

rf = driver.find_element(By.LINK_TEXT, '認證整修品')
rf.click()
time.sleep(1)
rf_mac = driver.find_element(By.XPATH, '//*[@id="refurb-landing"]/div/div[1]/div/ul/li[1]/a')
rf_mac.click()
time.sleep(10)

all_products = []

while True:
    products = driver.find_elements(By.CLASS_NAME, 'rf-refurb-producttile')
    for product in products:
        title = product.find_element(By.CLASS_NAME, 'rf-refurb-producttile-link').text
        price = product.find_element(By.CSS_SELECTOR, 'span.rf-refurb-producttile-currentprice').text
        link = product.find_element(By.CLASS_NAME, 'rf-refurb-producttile-link')

        p = {}
        p['title'] = title
        p['price'] = price
        p['link'] = link.get_attribute('href')
        all_products.append(p)
    btn = driver.find_element(By.XPATH, '//*[@id="root"]/div/nav/div/div[3]/button')
    if btn.get_attribute('disabled'):
        break
    btn.click()
    time.sleep(2)
print(f'共找到{len(all_products)}筆整修品')
for product in all_products:
    print(f'商品名稱：{product['title']}')
    print(f'價格：{product['price']}')
    print('*' * 100)
    ws.append([product['title'],product['price'],product['link']])
# print(len(all_products))

wb.save('apple.xlsx')

driver.quit()