from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time


# 크롬 드라이버 생성
driver = webdriver.Chrome()

# 페이지 이동
driver.get("https://search.shopping.naver.com/search/all?query=%EB%8B%AD%EA%B0%80%EC%8A%B4%EC%82%B4")

last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # 스크롤 끝까지 내리기
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)

    # 스크롤 후 높이
    new_height = driver.execute_script("return document.body.scrollHeight")

    # 비교 (if, break)
    if new_height == last_height:
        break

    # 스크롤 전 높이 업데이트
    last_height = new_height

# 상품명, 상세페이지링크, 가격 추출
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

data = []
items = soup.select(".product_item__MDtDF")
for item in items:
    name = item.select_one(".product_title__Mmw2K > a").text
    link = item.select_one(".product_title__Mmw2K > a").attrs["href"]
    price = int(item.select_one(".price_num__S2p_v").text.replace(',', '').replace('원', ''))
    if item.select_one("[data-shp-area-id='purchasecount'] em"):
        purchase = item.select_one("[data-shp-area-id='purchasecount'] em").text.replace(',', '')
        if '만' in purchase:
            purchase = int(float(purchase.split('만')[0]) * 10000)
    else:
        purchase = ''
    data.append([name, link, price, purchase])

df = pd.DataFrame(data, columns=['상품명', '상세페이지링크', '가격', '구매수'])
df.to_excel("naver_shopping_crawling.xlsx")

# 웹드라이버 종료
driver.quit()