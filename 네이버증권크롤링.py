import requests
from bs4 import BeautifulSoup
import pandas as pd

data = []
for i in range(1, 1000):
    response = requests.get(f'https://finance.naver.com/news/mainnews.naver?date=2024-08-26&page={i}')
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    articles = soup.select(".block1")
    for article in articles:
        title = article.select_one(".articleSubject > a").text
        link = 'https://finance.naver.com' + article.select_one(".articleSubject > a").attrs['href']
        content = article.select_one(".articleSummary").contents[0].strip()
        press = article.select_one(".press").text.strip()
        date = article.select_one(".wdate").text
        print(title, link, content, press, date)
        data.append([title, link, content, press, date])

    if soup.select_one(".pgRR") == None:
        break

df = pd.DataFrame(data, columns=['제목', '링크', '내용', '언론사', '날짜'])
df.to_excel("naver_finance_crawling.xlsx")