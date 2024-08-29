from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pyperclip

# 크롬 드라이버 생성
driver = webdriver.Chrome()

# 페이지 이동
driver.get("https://nid.naver.com/nidlogin.login?mode=form&url=https://www.naver.com/")
time.sleep(1)

# 계정정보
uset_id = 'wlsgurlek'
uset_pw = 'good0902!!'
email = 'wlsgurlek@naver.com'

# 아이디 입력
id = driver.find_element(By.CSS_SELECTOR, "#id")
pyperclip.copy(uset_id)
id.send_keys(Keys.CONTROL, 'v')
time.sleep(1)

# 비밀번호 입력
pw = driver.find_element(By.CSS_SELECTOR, "#pw")
pyperclip.copy(uset_pw)
pw.send_keys(Keys.CONTROL, 'v')
time.sleep(1)

# 로그인 버튼 클릭
driver.find_element(By.CSS_SELECTOR, "#log\\.login").click()
time.sleep(1)
#
driver.find_element(By.CSS_SELECTOR, "#new\\.save").click()
# 드롭다운 메뉴 클릭
driver.find_element(By.CSS_SELECTOR, "#account > div.MyView-module__my_menu___eF24q > div > div > ul > li:nth-child(1) > a > span.MyView-module__item_text___VTQQM").click()
time.sleep(1)
# 메일함 버튼 클릭
driver.find_element(By.CSS_SELECTOR, "#account > div.MyView-module__layer_menu_service___NqMyX > div.MyView-module__service_sub___wix9p > div.MyView-module__sub_left___AIWHR > a").click()

# 새창으로 전환
driver.switch_to.window(driver.window_handles[1])
time.sleep(2)
# 메일 쓰기 버튼 클릭
driver.find_element(By.CSS_SELECTOR, "#root > div > nav > div > div > div.lnb_task > a.item.button_write").click()
time.sleep(1)
# 받는 사람 입력
driver.find_element(By.CSS_SELECTOR, "#recipient_input_element").send_keys(email)

# 제목 입력
driver.find_element(By.CSS_SELECTOR, "#subject_title").send_keys('크롤링테스트')

# iframe 전환
iframe = driver.find_element(By.CSS_SELECTOR, "#content > div.contents_area > div.mail_write > div.editor_area > div.workseditor-classic > div.editor_body > iframe")
driver.switch_to.frame(iframe)

# 본문 입력
driver.find_element(By.CSS_SELECTOR, "body > div > div.workseditor-content").send_keys('내용내용내용')

# 보내기 버튼 클릭
driver.switch_to.default_content()
driver.find_element(By.CSS_SELECTOR, "#content > div.mail_toolbar.type_write > div.mail_toolbar_task > div.button_group > button").click()

# 웹드라이버 종료
driver.quit()
