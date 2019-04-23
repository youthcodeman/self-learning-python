#_*_ coding:utf-8 _*_
import time
import threading

def operation1(action1,loop) :
    for i in range(loop):
        print("do action:%s"%action1)
        time.sleep(1)

def operation2(action2,loop) :
    for i in range(loop):
        print("do action:%s"%action2)
        time.sleep(1)

t1 = threading.Thread(target = operation1,args=("操作1",3),name="operation1Thread")
t2 = threading.Thread(target = operation2,args=("操作2",5),name="operation1Thread")

if __name__ == "__main__":
   t1.start()
   t2.start()

   t1.join()   # 对主线程进行阻塞，等所有子线程运行结束在运行主线程
   t2.join()

   #守护主线程，主线程运行完成之后杀死所有子线程
   t1.setDaemon(True)
   t2.setDaemon(True)

   print(t1.ident)
   print(t2.ident)