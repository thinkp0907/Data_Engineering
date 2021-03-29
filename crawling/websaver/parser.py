## parser.py
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs
import pyperclip

## 아래 4줄을 추가해 줍니다.
import os
## Python이 실행될 때 DJANGO_SETTINGS_MODULE이라는 환경 변수에 현재 프로젝트의 settings.py파일 경로를 등록합니다.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "websaver.settings")
## 이제 장고를 가져와 장고 프로젝트를 사용할 수 있도록 환경을 만듭니다.
import django
django.setup()
## NavpayData를 import해옵니다
from parsed_data.models import NavpayData

driver = webdriver.Chrome('C:/Users/Chorlock/Downloads/chromedriver_win32/chromedriver')
driver.get('https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com')
# 로그인 자동 입력 방지를 위해 pyperclip 복사 붙여넣기 사용
pyperclip.copy('아이디')
driver.find_element_by_name('id').send_keys(Keys.CONTROL, 'v')
pyperclip.copy('비밀번호')
driver.find_element_by_name('pw').send_keys(Keys.CONTROL, 'v')
driver.find_element_by_xpath('//*[@id="log.login"]').click() # 버튼 클릭
driver.implicitly_wait(3)

def parse_Navpay():
    

    # Naver 페이 들어가기
    # 이게 있으면 넘어가고 없으면 안넘어감 why???
    driver.find_element_by_link_text('다음').click() 

    # 바로 넘어가지지 않음
    driver.get('https://order.pay.naver.com/home') # 네이버 페이
    html = driver.page_source ## 페이지 elements 모두 가져오기
    soup = bs(html, 'html.parser') # BeautifulSoup사용하기
    notices = soup.select('div.goods_item > div > a')
    notices = soup.select('div.goods_item > div > a > p')
    link = soup.select('div.goods_item > div > a')

    data = {}


    for n, l in zip(notices, link):
        data[n.text.strip()] = l.get('href')

    return data

## 이 명령어는 이 파일이 import가 아닌 python에서 직접 실행할 경우에만 아래 코드가 실행됩니다
if __name__ == '__main__':
    navpay_data_dict = parse_Navpay()
    for t, l in navpay_data_dict.items():
        NavpayData(title=t, link=l).save()