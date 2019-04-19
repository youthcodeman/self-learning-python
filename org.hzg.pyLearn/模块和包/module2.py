#_*_ coding:utf-8 _*_

# from math import *  #导入该模块下的所有模块
#
# print(ceil(1.5))
#
# print(floor(1.5))

import time as t
print(t.ctime())

#跨模块引用 用包.模块名
#不在统一目录下
import sys
sys.path.append("把需要导入模块的路径添加到python的sys里面")