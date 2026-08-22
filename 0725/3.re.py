#圖片爬蟲
import os
import re
import requests
import bs4
import urllib.request as req

url = 'https://www.tenlong.com.tw/zh_tw/recent?stock=preorder'

response = requests.get(url)

htmlfile = bs4.BeautifulSoup(response.text,'html.parser')

os.makedirs('img',exist_ok=True) #建立資料夾
books = htmlfile.find_all('li',class_='single-book')
for i,book in enumerate(books):
    title = book.select_one('.title a') .text #title裡面的a
    title = re.sub(r'[\\/?<>:|]','_',title)
    title = re.sub(r'[\x00-\x1f]','',title)
    img_url = book.find('img')['src']
    print(img_url)
    req.urlretrieve(img_url,f'img/{i}.jpg') #抓取圖片檔