#pip install googletrans==4.0.0-rc1
#구글 번역기를 사용하기 위한 라이브러리

import googletrans

translator = googletrans.Translator()

str1 = "행복하세요"
result1 = translator.translate(str1, dest='en', src='auto')
print(f"{str1} => {result1.text}")

str2 = "I am happy"
result2 = translator.translate(str2, dest='ko', src='en')
print(f"{str2} => {result2.text}")