from info import info
import requests
import json
import imaplib
import email
from email import policy

url = info.url()  # 카톡 인증 url
rest_api_key = info.rest_api_key()  # 카톡 rest 키
redirect_uri = info.redirect_uri()  # 카톡 인증용 redirect url
authorize_code = info.authorize_code()  # 카톡 인증용 코드 수행시마다 재발급 필요


# 최초 token들 발급하여 refresh token 저장
def f_get_refresh_token():
    data = {
        'grant_type': 'authorization_code',
        'client_id': rest_api_key,
        'redirect_uri': redirect_uri,
        'code': authorize_code,
    }

    response = requests.post(url, data=data)
    tokens = response.json()

    with open('refresh_token.json', 'w') as fd:
        json.dump(tokens, fd)


# refresh token을 이용하여 새로운 access token 발급
def f_reissue_token():
    with open('refresh_token.json', 'r') as fd:
        token = json.load(fd)
    print(token)
    refresh_token = token['refresh_token']
    data = {
        'grant_type': 'refresh_token',
        'client_id': rest_api_key,
        'refresh_token': refresh_token
    }
    response = requests.post(url, data=data)
    tokens = response.json()

    with open('access_token.json', 'w') as fd:
        json.dump(tokens, fd)
    with open('access_token.json', 'r') as fd:
        ts = json.load(fd)
    access_token = ts['access_token']
    return access_token


# 메시지 전송
def f_send_msg(access_token, msg):
    header = {'Authorization': 'Bearer ' + access_token}
    url = 'https://kapi.kakao.com/v2/api/talk/memo/default/send'  # 나에게 보내기 주소
    post = {
        'object_type': 'text',
        'text': msg,
        'link': {
            'web_url': 'https://developers.kakao.com',
            'mobile_web_url': 'https://developers.kakao.com'
        },
        'button_title': '키워드'
    }
    data = {'template_object': json.dumps(post)}
    return requests.post(url, headers=header, data=data)

def find_encoding_info(txt):
    info = email.header.decode_header(txt)
    subject, encode = info[0]
    return subject, encode

imap = imaplib.IMAP4_SSL('imap.naver.com')
id = info.naver_id()
pw = info.naver_pw()
imap.login(id,pw)

imap.select('INBOX')
resp, data = imap.uid('search', None, 'All')
all_email = data[0].split()
last_email = all_email[-5:]

for mail in reversed(last_email):
    result, data = imap.uid('fetch', mail, '(RFC822)')
    raw_email = data[0][1]
    email_message = email.message_from_bytes(raw_email, policy=policy.default)


    email_from = email_message['From']
    email_date = email_message['Date']
    subject,encode = find_encoding_info(email_message['Subject'])
    subject_str = str(subject)

    if subject_str.find("결제") >= 0:
        kakao_send_message = email_from + '\n' + email_date + '\n' + subject_str
        #f_get_refresh_token()
        access_token = f_reissue_token()  # 새로운 액세스 토큰을 발급 받음
        f_send_msg(access_token, kakao_send_message)
