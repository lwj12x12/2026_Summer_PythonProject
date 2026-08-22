import requests
import openpyxl
wb = openpyxl.Workbook()
ws = wb.active

ws.append(['類型','標題','地址','金額'])

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36'
}
for i in range(0,210,30):
    print(i)

    url = f'https://bff-house.591.com.tw/v3/web/rent/list?regionid=6&firstRow={i}'

    response = requests.get(url, verify=False, headers=header)

    # print(response.json())
    json_data = response.json()
    for item in json_data['data']['items']:
        print(item['kind_name'])
        print(item['title'])
        print(item['address'])
        print(item['price'])
        print('=' * 100)

        ws.append([item['kind_name'],item['title'],item['address'],item['price']])

wb.save('591.xlsx')