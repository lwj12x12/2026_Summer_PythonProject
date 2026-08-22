#圖片爬蟲
import requests
import bs4

url = 'https://www.tenlong.com.tw/zh_tw/recent?stock=preorder'

response = requests.get(url)

htmlfile = bs4.BeautifulSoup(response.text,'html.parser')


# print(htmlfile)

# imgs = htmlfile.find_all('img')
# for img in imgs:
#     try:
#         print(img['alt'])
#         print(img['src'])
#         print('-'*100)
#     except:
#         continue
books = htmlfile.find_all('li',class_='single-book')
for book in books:
    title = book.select_one('.title a') .text #title裡面的a
    img_url = book.find('img')['src']
    print(img_url)