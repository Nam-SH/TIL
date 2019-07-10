import requests
from bs4 import BeautifulSoup

url = 'https://www.naver.com/'
html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')
names = soup.select("#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li > a > span.ah_k")

# 1번째 방법
with open("naver_rank.txt", 'w', encoding='utf-8') as f:
    for name in names :
        f.write(f"{name.text}\n")

# 2번째 방법
with open("naver_rank2.txt", 'w') as f:
    for name in names :
        f.write(f"{name.text}\n") if name != names[-1] else f.write(f"{name.text}")

# 3번째 방법
with open("naver_rank3.txt", 'w', encoding='utf-8') as f:
    for name in names:
        rank = name.select_one('span.ah_r').text
        keyword = name.select_one('span.ah_k').text
        f.write(f'{rank}: {keyword}')