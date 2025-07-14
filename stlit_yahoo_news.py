import streamlit as st
from get_yahoo_news_titles import get_yahoo_news_titles

st.set_page_config(page_title="Yahoo!ニュース", layout="centered")

st.title("📰 Yahoo!ニュースまとめ")

with st.spinner("ニュースを取得中..."):
    try:
        titles = get_yahoo_news_titles()
        if titles:
            for t in titles:
                st.markdown(f"- {t}")
        else:
            st.warning("ニュースが取得できませんでした")
    except Exception as e:
        st.error(f"エラーが発生しました：{e}")