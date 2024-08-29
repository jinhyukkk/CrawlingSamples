import requests
from bs4 import BeautifulSoup
import pandas as pd
import urllib3

urllib3.disable_warnings()

data = []
param = {
    'isDetailSearch': 'N',
    'searchGubun': 'true',
    'viewYn': 'OP',
    'strQuery': '인공지능',
    'order': '/DESC',
    'onHanja': 'false',
    'strSort': 'RANK',
    'iStartCount': 0,
    'fsearchMethod': 'search',
    'sflag': 1,
    'isFDetailSearch': 'N',
    'pageNumber': 1,
    'icate': 're_a_kor',
    'colName': 're_a_kor',
    'pageScale': 10,
    'isTab': 'Y',
    'query': '인공지능'
}
response = requests.get('https://www.riss.kr/search/Search.do', params=param)
html = response.text
soup = BeautifulSoup(html, 'html.parser')
articles = soup.select(".srchResultListW > ul > li")

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    'Referer': 'https://www.riss.kr/search/Search.do?isDetailSearch=N&searchGubun=true&viewYn=OP&queryText=&strQuery=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5&exQuery=&exQueryText=&order=%2FDESC&onHanja=false&strSort=RANK&p_year1=&p_year2=&iStartCount=0&orderBy=&mat_type=&mat_subtype=&fulltext_kind=&t_gubun=&learning_type=&ccl_code=&inside_outside=&fric_yn=&db_type=&image_yn=&gubun=&kdc=&ttsUseYn=&l_sub_code=&fsearchMethod=search&sflag=1&isFDetailSearch=N&pageNumber=1&resultKeyword=&fsearchSort=&fsearchOrder=&limiterList=&limiterListText=&facetList=&facetListText=&fsearchDB=&icate=re_a_kor&colName=re_a_kor&pageScale=100&isTab=Y&regnm=&dorg_storage=&language=&language_code=&clickKeyword=&relationKeyword=&query=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5'
}

for article in articles:
    title = article.select_one(".title > a").text
    link = 'https://www.riss.kr/' + article.select_one(".title > a").attrs['href']

    # 상세페이지 요청
    response = requests.get(link, headers=header, verify=False)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    # 1. 순서를 기준으로 찾기
    # press = soup.select_one(".infoDetail > div > ul > li:nth-of-type(2) > div").text
    # year = soup.select_one(".infoDetail > div > ul > li:nth-of-type(5) > div").text
    # keywords = soup.select_one(".infoDetail > div > ul > li:nth-of-type(7) > div").text.split(';')

    # 2. 텍스트를 기준으로 찾기
    press = soup.find('span', string='발행기관').find_next_sibling().text
    year = soup.find('span', string='발행연도').find_next_sibling().text

    keywords = []
    if soup.find('span', string='주제어'):
        keywords = soup.find('span', string='주제어').find_next_sibling().text.split(';')
        keywords = [keyword.strip() for keyword in keywords]
    print(title, link, press, year, keywords)
