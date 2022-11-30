import re

test_string = '''
aaa@bbb.com
123@abc.co.kr
test@hello.kr
ok@ok.co.kr
ok@ok.co.kr
ok@ok.co.kr
no.co.kr
no.kr
'''

results = re.findall(r'[\w\.-]+@[\w\.-]+', test_string)

results = list(set(results)) #중복 항목 제거

print(f'이메일 정규식 테스트 : {results}')