#驅動程式
import streamlit as st

home = st.Page('home.py',title='首頁')
rate = st.Page('rate.py',title='匯率查詢')
rss = st.Page('rss.py',title='取得RSS')
weather = st.Page('weather.py',title='天氣資訊')
stock = st.Page('stock.py', title='股價查詢')

pg = st.navigation([home,rate,rss,weather,stock]) #導覽
pg.run()