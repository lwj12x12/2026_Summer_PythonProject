#首頁
import streamlit as st

st.title('首頁')
st.write('WELCOME~~')

with open('0822/basic.md','r', encoding='utf-8')as f:
    st.markdown(f.read())