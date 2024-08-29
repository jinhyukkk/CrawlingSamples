import requests
from bs4 import BeautifulSoup
import pandas as pd

data = []
page = int(input("몇 페이지까지 크롤링 하겠습니까?"))
for i in range(1, page + 1):
    response = requests.get(f'https://kin.naver.com/search/list.naver?query=%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90')
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    posts = soup.select(".basic1 > li")
    for post in posts:
        title = post.select_one("._nclicks\\:kin\\.txt").text
        link = post.select_one("._nclicks\\:kin\\.txt").attrs['href']
        date = post.select_one(".txt_inline").text
        category = post.select_one(".txt_block > a:nth-of-type(2)").text
        review = post.select_one(".txt_block > span:nth-of-type(2)").text.split('답변수')[1].strip()
        print(title, link, date, category, review)
        data.append([title, link, date, category, int(review)])

df = pd.DataFrame(data, columns=['제목', '링크', '날짜', '카테고리', '답변수'])
df.to_excel("naver_kin_crawling.xlsx")

