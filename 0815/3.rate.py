import requests
import bs4
from soupsieve import SelectorSyntaxError

while True:
    try:
        c = input('請輸入貨幣代號（cny,jpy,usd）或輸入q結束：')

        if c == 'q':
            print('掰!')
            break

        url = 'https://www.esunbank.com/zh-tw/personal/deposit/rate/forex/foreign-exchange-rates'

        response = requests.get(url)

        htmlfile = bs4.BeautifulSoup(response.text, 'html.parser')
        title = htmlfile.select_one(f'.{c.upper()} .title-item:nth-of-type(2)').text.strip()
        rate = htmlfile.select_one(f'.{c.upper()} .CashSBoardRate').text

        if rate=='':
            print(f'{title}沒有現金匯率')
        else:
            print(f'{title}匯率為{rate}')

    except AttributeError:
        print('請輸入正確的貨幣代號！')
        continue
    except SelectorSyntaxError:
        print('不可數字開頭！')
        continue