import streamlit as st

st.title('Hello! HERE is TITLE')
st.header('HEADER Here')
st.subheader('There is SUBHEADER')
st.write('WRITE is ME')

name = st.text_input('請輸入姓名：')
currency = st.selectbox(
    '選項',
    ['USD','JPY','EUR']
)
if st.button('ENTER'):
    st.write(name)
    st.write(currency)