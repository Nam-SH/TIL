from flask import Flask, render_template, request
from datetime import datetime 
import random
app = Flask(__name__)

@app.route('/')
def hello():
    # return 'Hello World!'
    return render_template("index.html")


@app.route('/ssafy')
def ssafy():
    return 'This is ssafy'


@app.route('/dday')
def dday():
    today_time = datetime.now() # 오늘 날짜가 필요
    end_game = datetime(2019, 11, 29) # 수료날짜
    dday = end_game - today_time # D-Day = 수려날짜 - 오늘 날짜
    return f'{dday.days}일 남았습니다...'


@app.route('/html')
def html():
    return '<h1>This is HTML TAG</h1>'


@app.route('/html_line')
def html_line():
    return """
    <h1>여러 줄을 보내 봅시다</h1>
    <ul>
        <li>1번</li>
        <li>2번</li>
    </ul>
    <ol>
        <li>1번</li>
        <li>2번</li>
    </ol>
    """

# @app.route('/greeting/: <string:name>')
@app.route('/greeting/<name>')
def greeting(name):
    # return f'반값습니다!! {name}'
    return render_template('greeting.html', html_name=name)


@app.route('/cube/<int:number>')
def cube(number):
    result = number**3
    # return f'{number}의 세제곱은 {number**3}입니다.'
    return render_template('cube.html', number=number, result=result)


@app.route('/movie')
def movie():
    movies = ['토이스토리', '스파이더맨', '알라딘', '기생충', '엔드게임']
    return render_template('movie.html', movies=movies)


@app.route('/lunch/<int:number>')
def lunch(number):
    menu = {'A음식', "B음식", "C음식", "D음식", "E음식"}
    choice = random.sample(menu, number)
    one = ", ".join(i for i in choice)
    return f'{number}명의 음식은 {one}입니다.'  


@app.route('/ping')
def ping():
    return render_template('ping.html')


@app.route('/pong')
def pong():
    key = request.args.get('key') #안녕하세요가 들어있음
    return render_template('pong.html', key=key)


# https://search.naver.com/search.naver
@app.route('/naver')
def naver():
    return render_template("naver.html")

# https://www.google.co.kr/search
@app.route('/google')
def google():
    return render_template("google.html")


@app.route('/nameinput')
def nameinput():
    return render_template('nameinput.html')

@app.route('/vonvon')
def vonvon():
    name = request.args.get('name')
    first_list = ['잘생김', '못생김', '어중간한']
    second_list = ['자신감', '쑥스러움', '애교', '잘난척']
    third_list = ['허세', '돈복', '식욕', '물욕', '성욕']
    
    first = random.choice(first_list)
    second = random.choice(second_list)
    third = random.choice(third_list)
    
    return render_template('vonvon.html', name=name, first=first, second=second, third=third)