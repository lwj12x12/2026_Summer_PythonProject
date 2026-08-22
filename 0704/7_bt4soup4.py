import requests
import bs4

url = 'https://www.ptt.cc/bbs/index.html'

response = requests.get(url)

print(response.text)

result = response.text

htmlfile = bs4.BeautifulSoup(result,'html.parser')
#print(htmlfile)
#print(htmlfile.find('a'))
#print(htmlfile.find_all('a'))

for item in htmlfile.find_all('a'):
    print(item)

#titles = htmlfile.find_all('div',{'class':title})
#titles = htmlfile.find_all('div',class_='title')

titles = htmlfile.find_all('div',class_='title')

for title in titles:
    print(title.find('a').text)

