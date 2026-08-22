import requests

url = 'https://data.moenv.gov.tw/api/v2/aqx_p_432?api_key=4c89a32a-a214-461b-bf29-30ff32a61a8a&limit=1000&sort=ImportDate desc&format=JSON'

response = requests.get(url,verify=False)

print(response.json())

for item in response.json():
    print(item['county'],item['status'])