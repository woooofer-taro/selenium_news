import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def get_yahoo_news():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://news.yahoo.co.jp/")
    items = driver.find_elements(By.CLASS_NAME, "newsFeed_item")

    news_list = []
    for item in items:
        try:
            link = item.find_element(By.TAG_NAME, "a").get_attribute("href")
            title = item.find_element(By.CLASS_NAME, "newsFeed_item_title").text.strip()
            if title:
                news_list.append({"title": title, "url": link})
        except:
            continue

    driver.quit()
    return news_list

# 保存
news = get_yahoo_news()
with open("yahoo_news.json", "w", encoding="utf-8") as f:
    json.dump(news, f, ensure_ascii=False, indent=2)
