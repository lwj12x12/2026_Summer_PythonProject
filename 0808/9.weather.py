import requests

url = 'https://api.openweathermap.org/data/2.5/weather?q=taipei,TW&appid=b1ecbccd638b763d489602917ba47cc3&units=metric&lang=zh_TW'
response = requests.get(url)

data = response.json()
temp = data['main']['temp']
temp_max = data['main']['temp_max']
temp_min = data['main']['temp_min']
feels = data['main']['feels_like']

desc = data['weather'][0]['description']

print(f'目前氣溫:{temp}\n最高溫:{temp_max}\n最低溫:{temp_min}\n體感溫度:{feels}\n{desc}')