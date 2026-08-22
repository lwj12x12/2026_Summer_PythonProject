import streamlit as st
import requests

st.title('天氣資訊')
q = st.text_input('請輸入城市名稱，如(taipei,tw)')

if st.button('取得天氣'):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={q}&appid=b1ecbccd638b763d489602917ba47cc3&units=metric&lang=zh_TW'
    response = requests.get(url)

    data = response.json()
    # print(type(data['cod']))
    if data['cod'] != 200:
        st.error('沒有該城市或發生錯誤')
    else:
        temp = data['main']['temp']
        temp_max = data['main']['temp_max']
        temp_min = data['main']['temp_min']
        feels = data['main']['feels_like']

        desc = data['weather'][0]['description']
        with st.container(border=True):
            st.image(f'https://openweathermap.org/payload/api/media/file/{data['weather'][0]['icon']}.png')
            st.write(f'目前氣溫:{temp}')
            st.write(f'最高溫:{temp_max}')
            st.write(f'最低溫:{temp_min}')
            st.write(f'體感溫度:{feels}\n{desc}')
