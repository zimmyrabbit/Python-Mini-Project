from info import info
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

send_email = info.naver_id()
send_pw = info.naver_pw()

print(send_email)

recv_email = info.naver_id()

smtp_name = 'smtp.naver.com'
smtp_port = 587

msg = MIMEMultipart()

msg['Subject'] = '첨부파일 전송 테스트'
msg['From'] = send_email
msg['To'] = recv_email

text = '''
첨부파일 메일 발송 테스트 입니다.
'''

contentPart = MIMEText(text)
msg.attach(contentPart)

etc_file_path = r'14.이메일 보내기\testfile.txt'

with open(etc_file_path, 'rb') as f :
    etc_part = MIMEApplication(f.read())
    etc_part.add_header('Content-Disposition','attachment', filename='testfile.txt')
    msg.attach(etc_part)

s = smtplib.SMTP(smtp_name, smtp_port)
s.starttls()
s.login(send_email, send_pw)
s.sendmail(send_email, recv_email, msg.as_string())
s.quit()