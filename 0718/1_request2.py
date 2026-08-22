from gettext import find

import requests
import bs4

url = 'https://www.ptt.cc/bbs/WorldCup/index1644.html'

response = requests.get(url)

# result = response.text
# htmlfile = bs4.BeautifulSoup(result,'html.parser')

htmlfile = bs4.BeautifulSoup(response.text,'html.parser')

rent = htmlfile.find_all('div',class_='r-ent')
for item in rent:
    if item.find('a') is None:
        continue
    if item.find('span') is None:
        continue
    print(item.find('span',class_='hl').text)
    print(item.find('div', class_='title').find('a').text)
    print(item.find('div', class_='author').text)
    print(item.find('div',class_='date').text)
    print(item.find('div',class_='mark').text)
    print('-' * 50)