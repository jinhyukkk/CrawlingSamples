# 셀레니움 기본 템플릿
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 크롬 드라이버 생성
driver = webdriver.Chrome()
# 원하는 페이지 이동
driver.get("https://startcoding.pythonanywhere.com/basic")

# 태그 찾기
labels = driver.find_elements(By.CSS_SELECTOR, "label[for]")

for label in labels:
    print(label.text, label.get_attribute("for"))
    label.click()