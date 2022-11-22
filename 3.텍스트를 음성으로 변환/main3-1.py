#pip install gtts
#문자 음성변환 라이브러리

#pip install playsound==1.2.2
# mp3 파일을 파이썬에서 재생하기 위한 라이브러리

from gtts import gTTS

text = "안녕하세요 이진채 입니다."

tts = gTTS(text=text, lang='ko')
tts.save(r"3.텍스트를 음성으로 변환\hi.mp3")