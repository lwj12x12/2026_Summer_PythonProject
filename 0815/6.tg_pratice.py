import requests
import bs4
from dotenv import load_dotenv
import os

from soupsieve import SelectorSyntaxError

load_dotenv()
# 常數
TOKEN = os.getenv('TOKEN')
GET_UPDATES_URL = f'https://api.telegram.org/bot{TOKEN}/getUpdates'
SEND_MESSAGES_URL = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
rss_web = {
    'twse':'https://www.twse.com.tw/rwd/zh/news/feed?type=rss',
    'mohw' :'https://www.mohw.gov.tw/rss-16-1.html',
    'moi': 'https://www.moi.gov.tw/OpenData.aspx?SN=76F358C679FAD4CF'
}

update_id = 0

def get_rate(c):
    try:
        url = 'https://www.esunbank.com/zh-tw/personal/deposit/rate/forex/foreign-exchange-rates'
        response = requests.get(url)
        htmlfile = bs4.BeautifulSoup(response.text, 'html.parser')
        title = htmlfile.select_one(f'.{c.upper()} .title-item:nth-of-type(2)').text.strip()
        rate = htmlfile.select_one(f'.{c.upper()} .CashSBoardRate').text
        if rate == '':
            print(f'{title}沒有現金匯率')
            return f'{title}沒有現金匯率'
        else:
            # print(f'{title}匯率為{rate}')
            return f'{title}匯率為{rate}'

    except AttributeError:
        print('請輸入正確的貨幣代號！')
        return '請輸入正確的貨幣代號！'
    except SelectorSyntaxError:
        return '不可數字開頭！'


def get_weather(q):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={q}&appid=b1ecbccd638b763d489602917ba47cc3&units=metric&lang=zh_TW'
    # metric:攝氏 imperial華氏
    response = requests.get(url)

    data = response.json()
    # print(type(data['cod']))
    if data['cod'] != 200:
        return '沒有該城市或發生錯誤'
    else:
        temp = data['main']['temp']
        temp_max = data['main']['temp_max']
        temp_min = data['main']['temp_min']
        feels = data['main']['feels_like']

        desc = data['weather'][0]['description']

        return f'目前氣溫:{temp}\n最高溫:{temp_max}\n最低溫:{temp_min}\n體感溫度:{feels}\n{desc}'

def get_rss(url):
    response = requests.get(url, verify=False)
    soup = bs4.BeautifulSoup(response.text, 'xml')
    items = soup.find_all('item')
    rss = []
    for item in items:
        title = item.find('title').text
        # title = item.title.text
        rss.append({'title': title, 'pubDate': item.pubDate.text})
    return rss


while True:
    try:
        param = {
            'offset': update_id,
            'timeout': 30
        }
        response = requests.get(GET_UPDATES_URL, params=param, timeout=35)
        data = response.json()
        for update in data['result']:
            update_id = update['update_id'] + 1
            chat_id = update['message']['chat']['id']
            user_text = update['message']['text']

            #匯率
            # if user_text == '/rate':
            #     user_text = get_rate()
            if user_text.startswith('/rate'):
                cmd = user_text.split()
                user_text = get_rate(cmd[1])
                print(cmd)
            # weather
            if user_text.startswith('/weather'):
                cmd = user_text.split()
                user_text = get_weather(cmd[1])

            if user_text.startswith('/rss'):
                cmd = user_text.split()
                rss_url = rss_web[cmd[1]]
                datas = get_rss(rss_url)[:10] #10筆資料
                user_text = ''
                for data in datas:
                    user_text += f'{data['title']}\n{data['pubDate']}\n\n'
                    user_text += '='*30
                    user_text += '\n'

            # /start
            if user_text == '/start':
                user_text = 'Hello 我是你的激起人!!!'

            send_data = {'chat_id': chat_id, 'text': user_text}
            send_msg = requests.post(SEND_MESSAGES_URL, data=send_data, timeout=30)

    except Exception as e:
        print('error')
        print(e)
        continue