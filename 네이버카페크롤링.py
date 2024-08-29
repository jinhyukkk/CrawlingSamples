from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd
import time


# 크롬 드라이버 생성
driver = webdriver.Chrome()

# 페이지 이동
driver.get("https://cafe.naver.com/startcodingofficial")

# 유투브 후기 게시판 클릭 : id 값으로 태그 찾기
driver.find_element(By.CSS_SELECTOR, "#menuLink15").click()

# iframe 전환
iframe = driver.find_element(By.CSS_SELECTOR, "#cafe_main")
driver.switch_to.frame(iframe)

# 50개씩 표시하기 클릭
# ElementNotInteractableException : 태그가 안보여서 클릭할 수 없음
element = driver.find_element(By.CSS_SELECTOR, "#listSizeSelectDiv > ul > li:nth-child(7) > a")

# 1. 태그를 보이게 만들고 클릭 실행
driver.find_element(By.CSS_SELECTOR, "#listSizeSelectDiv > a").click()
element.click()

# 2. JavaScript를 이용하여 태그 클릭 실행
# StaleElementException : 페이지가 갱신되어서 태그가 유효하지 않을 경우 방생
driver.execute_script("arguments[0].click();", element)

# 글 목록 추출하기 (일반글)
posts = driver.find_elements(By.CSS_SELECTOR, ".article-board.m-tcol-c:not(#upperArticleList) .article")
print(posts)
for post in posts:
    title = post.text
    link = post.get_attribute("href")
    print(title, link)