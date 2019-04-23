#_*_ coding:utf-8 _*_
import threading

balance = 0

def change(n) :
    global balance
    balance += n
    balance -= n

# def run_thread(n) :
#     for i in range(1000000) :
#         change(n)

lock = threading.Lock()
def run_thread(n) :
    lock.acquire()
    try:
        for i in range(1000000) :
            change(n)
    except(Exception):
        print("哈哈哈，异常了")
    finally:
        lock.release()

t1 = threading.Thread(target=run_thread,args=(4,))
t2 = threading.Thread(target=run_thread,args=(8,))
if __name__ == "__main__":
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(balance)