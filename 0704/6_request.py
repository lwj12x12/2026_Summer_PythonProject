import requests
import bs4

url = ''

response = requests.get(url)

print(response.text)