import requests
from bs4 import BeautifulSoup

html = requests.get('https://finance.naver.com/marketindex/').text
soup = BeautifulSoup(html, 'html.parser')
exchange = soup.select_one('#worldExchangeList > li.on > a.head.jpy_usd > div > span.value').text\

print(exchange)