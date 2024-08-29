from selenium import webdriver
driver = webdriver.Chrome()
# 원하는 페이지 이동
driver.get("https://www.naver.com")
# 뒤로가기
driver.back()
# 앞으로가기
driver.forward()
# 새로고침
driver.refresh()
# 현재 URL 확인
driver.current_url
# 페이지 제목 확인
driver.title
# 최대화
driver.maximize_window()
# 최소화
driver.minimize_window()
# 현재 창 닫기
driver.close()
# 모든 창을 닫고, 웹드라이버 세션 종료
driver.quit()

