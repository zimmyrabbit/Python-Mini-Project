#pip install psutil
#컴퓨터의 정보를 확인할때 사용하는 라이브러리

import psutil

cpu = psutil.cpu_freq()
print('cpu 속도 : ', cpu)

cpu_core = psutil.cpu_count(logical=False)
print('cpu 물리코어 수 : ', cpu_core)

memory = psutil.virtual_memory()
print('메모리 정보 : ', memory)

disk = psutil.disk_partitions()
print('디스크 정보 : ', disk)

net = psutil.net_io_counters()
print('네트워크를 통해 보내고 받은 데이터량 : ', net)