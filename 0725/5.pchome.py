import requests
import bs4
import urllib.request as req
import os

url = 'https://24h.pchome.com.tw/region/DRAD?srsltid=AfmBOoo4v9ub-0bBKby29PEOJkHi-ZBqhR9K3IO5SPjWpyR5Ku9FiycW'

response = requests.get(url)

# print(response.status_code)
htmlfile = bs4.BeautifulSoup(response.text, 'html.parser')
imgs = htmlfile.select('.c-puzzleCard__img img')
os.makedirs('pchome', exist_ok=True)
for i,img in enumerate(imgs):
    print(img['src'])

    req.urlretrieve(img['src'], f'pchome/{i}.jpg')