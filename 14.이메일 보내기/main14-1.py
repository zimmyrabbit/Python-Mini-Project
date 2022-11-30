from info import info
import smtplib
from email.mime.text import MIMEText

send_email = info.naver_id()
send_pw = info.naver_pw()

print(send_email)

recv_email = info.naver_id()

smtp_name = 'smtp.naver.com'
smtp_port = 587

text = '''
네이버 메일 발송 테스트 입니다.
'''

msg = MIMEText(text)

msg['Subject'] = '메일 제목'
msg['From'] = send_email
msg['To'] = recv_email
print(msg.as_string())

s=smtplib.SMTP(smtp_name, smtp_port)
s.starttls()
s.login(send_email, send_pw)
s.sendmail(send_email, recv_email, msg.as_string())
s.quit()