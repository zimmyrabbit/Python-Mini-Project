import qrcode
import os

file_path = os.path.dirname(os.path.abspath(__file__)) + '\qr코드모음.txt'

with open(file_path, 'r', encoding='UTF8') as f:
    read_lines = f.readlines()

    for line in read_lines:
        line = line.strip()
        print(line)