#pip install qrcode
#QR CODE 라이브러리
#https://pypi.org/project/qrcode/

import qrcode
import os

qr_data = 'www.github.com/zimmyrabbit'
qr_img = qrcode.make(qr_data)

save_path = os.path.dirname(os.path.abspath(__file__)) + '\\zimmyrabbit.png'

qr_img.save(save_path)