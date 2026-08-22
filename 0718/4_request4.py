import requests

url = 'https://bff-house.591.com.tw/v3/web/rent/list?timestamp=1784346830976&regionid=6&firstRow=30'

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36'
}

response = requests.get(url, verify=False, headers=header)

#print(response.status_code)

print(response.json())
json_data = response.json()
for item in json_data['data']['items']:
    print(item['kind_name'])
    print(item['title'])
    print(item['address'])
    print(item['price'])
    print("="*100)