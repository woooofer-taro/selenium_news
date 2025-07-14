import streamlit as st
import json
import requests

# GitHubからJSON読み込み
URL = "https://raw.githubusercontent.com/USERNAME/REPO/main/yahoo_news.json"

st.title("📰 Yahoo!ニュース（キャッシュ表示）")

try:
    res = requests.get(URL)
    news = res.json()

    for item in news:
        st.markdown(f"- [{item['title']}]({item['url']})")

except Exception as e:
    st.error(f"読み込み失敗: {e}")
