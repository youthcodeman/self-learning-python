#_*_ coding:utf-8 _*_

import os

print(os.getcwd()) #获取当前目录所在的绝对路径

print(os.listdir("F://")) #指定文件夹下面的所有内容

print(os.path.isfile("file1.txt")) # 是否是问价

print(os.path.exists("file1.txt"))  #文件是否存在

os.renames() # 重命名
