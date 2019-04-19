#_*_ coding:utf-8 _*_
import time  #导入整个模块

print("start")
time.sleep(5)
print("stop")

from time import ctime  #从某个模块导入另一个模块
print(ctime())

from time import sleep
print("start")
sleep(5)
print("stop")