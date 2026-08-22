import streamlit as st
import yfinance

st.title('股價查詢')

code = st.text_input('請輸入股票代號，如(2330.TW)')

if st.button('取得股價'):
    data = yfinance.Ticker(f'{code}')
    # st.success(f'{code}目前股價為{data.fast_info['lastPrice']}')
    st.write(data.fast_info['lastPrice'])