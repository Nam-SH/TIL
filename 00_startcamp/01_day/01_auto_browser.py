import webbrowser

# 1. 리스트가 필요
a = ["www.google.com", "www.naver.com", "www.daum.net"]

for i in a:
    webbrowser.open_new_tab(i)

idols = ["bts", "nrg", "hot", "babyvox"]
url = 'https://search.naver.com/search.naver?query='

for idol in idols:
    webbrowser.open_new(url+idol)

import requests

response = requests.get('https://www.google.co.kr/').status_code
print(response)

from bs4 import BeautifulSoup


