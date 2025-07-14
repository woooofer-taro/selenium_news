from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def get_yahoo_news_titles():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # ← 表示しないモード（開発中は外してもOK）
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    driver.get("https://news.yahoo.co.jp/")

    # Yahooニュースのタイトル（記事見出し）取得
    elements = driver.find_elements(By.CLASS_NAME, "newsFeed_item_title")

    titles = [e.text for e in elements if e.text.strip() != ""]
    driver.quit()
    return titles
