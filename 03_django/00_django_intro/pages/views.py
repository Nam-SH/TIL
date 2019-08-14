# django import style guide
# 1. standard library
# 2. third-pardy (request ...)
# 3. Django
# 4. local django


import random
from datetime import datetime
from django.shortcuts import render

# Create your views here.
def index(request): # 첫 번째 인자는 반드시 request
    return render(request, 'index.html') # render()의 첫 번재 인자도 반드시 request


def introduce(request, name, age):
    context = {'name': name, 'age': age,}
    return render(request, 'introduce.html', context)


def dinner(request):
    menu = ['족발', '햄버걸', '취킨', '김밥']
    pick = random.choice(menu)
    context = {'pick': pick}
    return render(request, 'dinner.html', context)


def image(request):
    return render(request, 'image.html')


def hello(request, name):
    menu = ['족발', '햄버걸', '취킨', '김밥']
    pick = random.choice(menu)
    context = {'pick': pick, 'name': name,}
    return render(request, 'hello.html', context)


def times(request, num1, num2):
    num3 = num1 * num2
    context = {'num3': num3, 'num1': num1, 'num2': num2,}
    return render(request, 'times.html', context)


def template_language(request):
    menus = ['자장면', '탕수육', '라조기', '양장피', '찜뽕',]
    my_sentence = 'Life is short, you need python'
    messages = ['apple', 'banana', 'cucumber', 'bean',]
    datetimenow = datetime.now()
    empty_list = []
    context = {
      'menus': menus,
      'my_sentence': my_sentence,
      'messages': messages,
      'empty_list': empty_list,
      'datetimenow': datetimenow,
    }
    return render(request, 'template_language.html', context)

def isitgwangbok(request):
    today = datetime.now()
    if today.month == 8 and today.day == 15:
        result = True
    else:
        result = False
    context = {'result': result}
    return render(request, 'isitgwangbok.html', context)