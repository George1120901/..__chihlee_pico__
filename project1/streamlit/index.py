import streamlit as st
from streamlit_autorefresh import st_autorefresh
import requests
import pandas

#自動reload頁面每2秒
st_autorefresh(interval=2000, limit=100, key="fizzbuzzcounter")

testURL = 'http://127.0.0.1:8000/items/10'
response = requests.post(testURL)
if response.ok:
    json_data = response.json()
    data_df = pandas.DataFrame(json_data)


st.title('PICO_W-距離和亮度測試')

st.header('高度:')
st.line_chart(data_df,y='light')

st.header('距離:')
st.line_chart(data_df,y='distance')

