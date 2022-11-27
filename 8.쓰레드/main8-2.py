import threading
import time

def thread_1():
    while True:
        print("쓰레드1 동작")
        time.sleep(1.0)

t1 = threading.Thread(target=thread_1)
# 쓰레드를 데몬쓰레드로 지정 메인쓰레드가 동작할때만 동작하도록 
t1.daemon = True
t1.start()

while True:
    print("메인동작")
    time.sleep(2.0)