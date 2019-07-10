import smtplib
from email.message import EmailMessage
import getpass

password = getpass.getpass('PASSWORD: ')

msg = EmailMessage()
msg['Subject'] = '권고사직서'
msg['From'] = '666murderer@naver.com'
msg['To'] = 'gtsmell@gmail.com'
msg.set_content('죄쇵합니다..')

ssafy = smtplib.SMTP_SSL('smtp.naver.com', 465)
ssafy.login('666murderer', password)

ssafy.send_message(msg)

print('이메일 전송 완료')