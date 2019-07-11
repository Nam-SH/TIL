import requests
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/lotto_check')
def lotto_check():
    return render_template("lotto_check.html")


@app.route('/lotto_result')
def lotto_result():
    num = requests.arg.get('num')
    res = requests.get(f'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={num}')
    lotto = res.json()
    
    winner = []
    for i in range(7):
        winner.append(lotto[f'drwtNo{i}'])
    
    numbers = []
    for num in requests.args.get('numbers').split():
        numbers.append(int(num))

    matched = 0
    for num in numbers:
        if num in winner:
            matched += 1
        if matched == 6:
            result = "1등입니다."
        elif matched == 5:
            if lotto['bnusNo'] in numbers:
                result = "2등입니다."
            else:
                result = "3등입니다."
        elif matched == 4:
            result = "4등입니다."
        elif matched == 3:
            result = "5등입니다."
        else:
            result = "꽝입니다."

    return render_template("lotto_check.html")


