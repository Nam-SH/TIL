# 1. BotFather



# 2. bot name setting : nam / nam_ssafy_bot



# 3. Use this token to access the HTTP API:

862920006:AAFTN_2yIG0EGDDOVY-gU0mck004asSmFKQ



# 4. METHOD_NAME : getMe

https://api.telegram.org/bot<token>/METHOD_NAME

https://api.telegram.org/bot862920006:AAFTN_2yIG0EGDDOVY-gU0mck004asSmFKQ/getMe

"ok": true,
  "result": {
    "id": 862920006,
    "is_bot": true,
    "first_name": "nam",
    "username": "nam_ssafy_bot"

# 5. METHOD_NAME : getUpdates

###### https://api.telegram.org/bot862920006:AAFTN_2yIG0EGDDOVY-gU0mck004asSmFKQ/getUpdates

"chat": {
          "id": 873957605,

# 6. METHOD_NAME : sendMessage

https://api.telegram.org/bot<token>/sendMessage?chat_id=<chat_id>&text=안녕하세요

https://api.telegram.org/bot862920006:AAFTN_2yIG0EGDDOVY-gU0mck004asSmFKQ/sendMessage?chat_id=873957605&text=안녕하세요

# 7. pip install python-decouple

token 값 가리기



# 8. app.py



# 9. ngrok

포트 열어주는 것

cd ~ 경로에 넣기

cmd창 열고, `ngok http 5000 입력` --> 계속 띄어놓기

```
Session Status                online
Session Expires               7 hours, 59 minutes
Version                       2.3.30
Region                        United States (us)
Web Interface                 http://127.0.0.1:4040
Forwarding                    http://a17b69fe.ngrok.io -> http://localhost:5000
Forwarding                    https://a17b69fe.ngrok.io -> http://localhost:5000

Connections                   ttl     opn     rt1     rt5     p50     p90
                              0       0       0.00    0.00    0.00    0.00
```



# 10. webhook 등록 주소

https://api.telegram.org/bot<token>/setWebhook?url=<ngrok-forwarding-http-url>/<token>



https://api.telegram.org/bot862920006:AAFTN_2yIG0EGDDOVY-gU0mck004asSmFKQ/setWebhook?url=https://a17b69fe.ngrok.io/862920006:AAFTN_2yIG0EGDDOVY-gU0mck004asSmFKQ



# 11. dep.naver : smt 파파고

**Client ID**: O82I2Eu48n8kJfR1m4Cq

**Client Secret**: lUsGfgrRFY



언어감지

Client ID: JP3xWKUfoIWoxg9jTKNU

Client Secret: aAJofmLg7y

# 12. python anywhere

mysite안의 flask에  app.py 복사 넣기

consoles안에 .env파일 만들고, .env 복사 넣기



# 13. webhook 등록 주소

https://api.telegram.org/bot<token>/setWebhook?url=<ngrok-forwarding-http-url>/<token>



https://api.telegram.org/bot862920006:AAFTN_2yIG0EGDDOVY-gU0mck004asSmFKQ/setWebhook?url=https://ssafy1.pythonanywhere.com/862920006:AAFTN_2yIG0EGDDOVY-gU0mck004asSmFKQ

