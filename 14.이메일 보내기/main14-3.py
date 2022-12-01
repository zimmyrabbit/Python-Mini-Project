from info import info
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#https://html5-editor.net/

send_email = info.naver_id()
send_pwd = info.naver_pw()

recv_email = info.naver_id()

smtp_name = 'smtp.naver.com'
smtp_port = 587

msg = MIMEMultipart()

msg['Subject'] = 'html로 보내는 메일'
msg['From'] = send_email
msg['To'] = recv_email

html_body = '''
<p>안녕하세요 html 형식으로 보내는 이메일 테스트 입니다.</p>
<p>&nbsp;</p>
<p><span style="color: #0000ff;">글자 색상 변경</span></p>
<p>&nbsp;</p>
<p><span style="color: #0000ff;">표 생성</span></p>
<table style="height: 79px;" width="239">
<tbody>
<tr>
<td style="width: 72.8625px;">1</td>
<td style="width: 72.8625px;">2</td>
<td style="width: 72.875px;">3</td>
</tr>
<tr>
<td style="width: 72.8625px;">a</td>
<td style="width: 72.8625px;">b</td>
<td style="width: 72.875px;">c</td>
</tr>
<tr>
<td style="width: 72.8625px;">ㄱ</td>
<td style="width: 72.8625px;">ㄴ</td>
<td style="width: 72.875px;">ㄷ</td>
</tr>
</tbody>
</table>
'''

msg.attach(MIMEText(html_body, 'html'))

s = smtplib.SMTP(smtp_name, smtp_port)
s.starttls()
s.login(send_email, send_pwd)
s.sendmail(send_email, recv_email, msg.as_string())
s.quit()