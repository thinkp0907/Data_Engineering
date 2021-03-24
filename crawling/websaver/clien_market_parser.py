# clien_market_parser.py

import requests
from bs4 import BeautifulSoup as bs
import os

import telegram

# 토큰을 지정해서 bot을 선언해 줍시다! 
bot = telegram.Bot(token='1667990389:AAHYkzv6hGXTznSCGpM0TYRorc8qs2FeO-8')
# 우선 테스트 봇이니까 가장 마지막으로 bot에게 말을 건 사람의 id를 지정해줄게요.
# 만약 IndexError 에러가 난다면 봇에게 메시지를 아무거나 보내고 다시 테스틓보세요.
# print(bot.getUpdates())
chat_id = bot.getUpdates()[-1].message.chat.id


# 파일의 위치
BASE_DIR = os.path.dirname(os.path.abspath('./crawling/'))

req = requests.get('https://www.clien.net/service/board/sold')
req.encoding = 'utf-8'

html = req.text
soup = bs(html, 'html.parser')
posts = soup.select('#div_content > div.list_content > div:nth-child(1) > div.list_title > a > span.subject_fixed')
latest = posts[0].text.strip()

with open(os.path.join(BASE_DIR, 'latest.txt'), 'r+', encoding='UTF-8') as f_read:
    before = f_read.readline()
    if before != latest:
        bot.sendMessage(chat_id=chat_id, text= latest + ' 라는 글이 올라왔어요!')
    else:
        bot.sendMessage(chat_id=chat_id, text='새 글이 없어요!ㅠㅠ')
    f_read.close()
    
with open(os.path.join(BASE_DIR, 'latest.txt'), 'w+', encoding='UTF-8') as f_write:
    f_write.write(latest)
    f_write.close()