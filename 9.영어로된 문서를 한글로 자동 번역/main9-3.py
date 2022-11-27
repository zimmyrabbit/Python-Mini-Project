from os import linesep
import googletrans

translator = googletrans.Translator()

read_file_path = r'9.영어로된 문서를 한글로 자동 번역\english.txt'

with open(read_file_path, 'r') as f:
    readLines = f.readlines()

for lines in readLines:
    result1 = translator.translate(lines, dest='ko', src='auto')
    print(result1.text)