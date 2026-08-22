import requests
import bs4

url = 'https://www.esunbank.com/zh-tw/personal/deposit/rate/forex/foreign-exchange-rates'

response = requests.get(url)

htmlfile = bs4.BeautifulSoup(response.text, 'html.parser')

usd = htmlfile.select_one('.USD .CashSBoardRate').text
cny = htmlfile.select_one('.CNY .CashSBoardRate').text
jpy = htmlfile.select_one('.JPY .CashSBoardRate').text

print(usd)
print(cny)
print(jpy)