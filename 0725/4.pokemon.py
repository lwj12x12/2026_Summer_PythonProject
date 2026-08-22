import os

import requests
import urllib.request as req

url = 'https://tw.portal-pokemon.com/play/pokedex/api/v1?pokemon_ability_id=&zukan_id_from=1&zukan_id_to=1025'
img_url = 'https://tw.portal-pokemon.com/play/resources/pokedex'

response = requests.get(url)
pokemons = response.json()
os.makedirs('qqq', exist_ok=True)
count = 0
for pokemon in pokemons['pokemons']:
    name = pokemon['pokemon_name']
    img = f'{img_url}{pokemon["file_name"]}'
    ext = os.path.splitext(img)[1]
    req.urlretrieve(img, f'qqq{name}.png')
    if count == 10:
        break
    count = count + 1
    # print(f'{img_url}{pokemon["file_name"]}')

