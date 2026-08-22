import requests
import bs4

while True:

    c = input('請輸入貨幣代號（cny,jpy,usd）或輸入q結束：')

    if c == 'q':
        print('掰!')
        break

    url = 'https://www.esunbank.com/zh-tw/personal/deposit/rate/forex/foreign-exchange-rates'

    response = requests.get(url)

    htmlfile = bs4.BeautifulSoup(response.text, 'html.parser')

    rate = htmlfile.select_one(f'.{c.upper()} .CashSBoardRate').text

    print(rate)