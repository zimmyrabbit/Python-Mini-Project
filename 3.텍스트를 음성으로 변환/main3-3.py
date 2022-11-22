from gtts import gTTS
from playsound import playsound
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

file_path = 'myText.txt'

with open(file_path, 'r', encoding='UTF8') as f:
    read_file = f.read()

tts = gTTS(text=read_file,lang='en')

tts.save("myText.mp3")

playsound("myText.mp3")