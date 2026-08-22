import requests
import bs4
url = 'https://www.twse.com.tw/rwd/zh/news/feed?type=rss'
response = requests.get(url)
soup = bs4.BeautifulSoup(response.text, 'xml')
items = soup.find_all('item')
for item in items:
    title = item.find('title').text
    content = item.find('content:encoded').text
    print(title)
    print(content)