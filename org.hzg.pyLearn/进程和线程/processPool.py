#_*_ coding:utf-8 _*_

import time
import multiprocessing

def work_1(f,n) :
    print("work_1 start")

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
        print("运行成功")

if __name__ == "__main__":
    pool = multiprocessing.Pool(3)
    for i in range(10) :
        pool.apply(work_1,args=("file.txt",2))

    pool.close()
    pool.join()
