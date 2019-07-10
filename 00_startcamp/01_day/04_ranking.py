import requests
from  bs4 import BeautifulSoup

html = ("https://www.naver.com/").text
soup = BeautifulSoup(html, "html.parser")
ranking = soup.select()