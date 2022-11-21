import socket

in_addr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#http의 기본 접속 포트 443
in_addr.connect(("www.google.co.kr", 443))

print(in_addr.getsockname()[0])