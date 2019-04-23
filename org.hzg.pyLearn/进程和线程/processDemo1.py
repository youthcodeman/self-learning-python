#_*_ coding:utf-8 _*_
import time
import multiprocessing

def work_1(f,n,lock) :
    print("work_1 start")
    lock.acquire()
    try:
        for i in range(n) :
            with open(f,"a") as fopen :
                fopen.write("hahahahhaha \n")
                fopen.flush()
                time.sleep(1)
            print("work1_finish")
    except(Exception ):
        print("捕获异常")
    finally:
        lock.release()


def work_2(f, n,lock):
    print("work_2 start")
    lock.acquire()
    try:
        for i in range(n):
            with open(f, "a") as fopen:
                fopen.write("i love my country \n")
                fopen.flush()
                time.sleep(1)
            print("work2_finish")
    except(Exception):
        print("捕获异常")
    finally:
        lock.release()

lock = multiprocessing.Lock()
p1 = multiprocessing.Process(target=work_1,args=("file.txt",5,lock))
p2 = multiprocessing.Process(target=work_2,args=("file.txt",5,lock))

if __name__ == "__main__":
    p1.start()
    p2.start()
    p1.join()
    p2.join()
