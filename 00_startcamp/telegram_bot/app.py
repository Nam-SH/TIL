from flask import Flask, render_template, request
import requests
from decouple import config
from bs4 import BeautifulSoup


app = Flask(__name__)
api_url = 'https://api.telegram.org'
token = config('TELEGRAM_BOT_TOKEN')
chat_id = config('CHAT_ID')
naver_client_id = config('NAVER_CLIENT_ID')
naver_client_secret = config('NAVER_CLIENT_SECRET')

@app.route('/')
def hello():
    return 'Hello'


@app.route(f'/{token}', methods=['POST'])
def telegram():
    from_telegram = request.get_json()
    
    if from_telegram.get('message') is not None:
        chat_id = from_telegram.get('message').get('from').get('id')
        text = from_telegram.get('message').get('text')
        headers = {
                'X-Naver-Client-Id': naver_client_id,
                'X-Naver-Client-Secret': naver_client_secret
            }
        if text == '/start':
            text = '명령 ㄱㄱ'

        if text[0:4] == '/영어 ':
            data = {'source': 'ko', 'target': 'en', 'text': text[4:]}
            papago_res = requests.post('https://openapi.naver.com/v1/papago/n2mt', headers=headers, data=data)
            text = papago_res.json().get('message').get('result').get('translatedText')
        
        elif text[0:6] == '/스페인어 ':
            data = {'source': 'ko', 'target': 'es', 'text': text[4:]}
            papago_res = requests.post('https://openapi.naver.com/v1/papago/n2mt', headers=headers, data=data)
            text = papago_res.json().get('message').get('result').get('translatedText')
        
        elif text[0:6] == '/베트남어 ':
            data = {'source': 'ko', 'target': 'vi', 'text': text[4:]}
            papago_res = requests.post('https://openapi.naver.com/v1/papago/n2mt', headers=headers, data=data)
            text = papago_res.json().get('message').get('result').get('translatedText')
        
        elif text[0:6] == '/프랑스어 ':
            data = {'source': 'ko', 'target': 'fr', 'text': text[4:]}
            papago_res = requests.post('https://openapi.naver.com/v1/papago/n2mt', headers=headers, data=data)
            text = papago_res.json().get('message').get('result').get('translatedText')
        
        elif text[0:4] == '/로또 ':
            num = text[4:]

            res = requests.get(f'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={num}')
            lotto = res.json()

            winner = []
            for i in range(1, 7):
                winner.append(lotto[f'drwtNo{i}'])
            bonus_num = lotto['bnusNo']
            winner = ", ".join(map(str, winner))
            text = f'{num}회차의 당첨 번호는 {winner} 입니다. 보너스 번호는 {bonus_num} 입니다.!!'

        elif text[0:6] == '/언어감지 ':
            naver_client_id = config('NAVER_CLIENT_DETECT_ID')
            naver_client_secret = config('NAVER_CLIENT_DETECT_SECRET')
            headers = {
                'X-Naver-Client-Id': naver_client_id,
                'X-Naver-Client-Secret': naver_client_secret
            }
            data = {'query':text[6:]}
            detect_res = requests.post('https://openapi.naver.com/v1/papago/detectLangs', headers=headers, data=data)
            text = detect_res.json().get("langCode")
            
        requests.get(f'{api_url}/bot{token}/sendMessage?chat_id={chat_id}&text={text}')

        if text[0:4] == '/코스피':
            html = requests.get('https://finance.naver.com/sise/').text
            soup = BeautifulSoup(html, 'html.parser')
            text = soup.select_one('#KOSPI_now').text

    
    return '', 200