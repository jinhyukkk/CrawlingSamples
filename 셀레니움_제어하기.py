# 셀레니움 기본 템플릿
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 크롬 드라이버 생성
driver = webdriver.Chrome()
# 원하는 페이지 이동
driver.get("https://www.naver.com")
# 태그 찾기
search = driver.find_element(By.CSS_SELECTOR, "#query")
# 1. 클릭
search.click()
# 2. 문자입력
search.send_keys("파이썬크롤링")
# 3. 키 입력
search.send_keys(Keys.ENTER)


