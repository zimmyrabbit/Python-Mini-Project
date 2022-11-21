import socket

in_addr = socket.gethostbyname(socket.gethostname())

#해당 방법으로 진행 시 가상 환경 등을 사용해 여러 개의 환경이 있을 경우 다른 환경의 IP가 출력 될 수 있음
print(in_addr)