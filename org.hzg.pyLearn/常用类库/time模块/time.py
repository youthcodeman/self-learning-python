#_*_ coding:utf-8 _*_
import time

# print(time.altzone)
#
# print(time.asctime())
#
# print(time.clock())

#返回当前时间的时间戳
# print(time.time())
# print(time.ctime())
#
# #返回一个时间元组（格林威治）
# print(time.gmtime())
#
# #返回当前时间的时间元组
# print(time.localtime())

#将时间戳转换为时间元组
times = time.time()
localTome = time.localtime(times)
print(localTome)
print(time.strftime("%Y-%m-%d %H:%M:%S" ,localTome))

#将时间字符串转换成时间元组
timeStr = "2019-04-22 00:07:11"
print(time.strptime(timeStr,"%Y-%m-%d %H:%M:%S" ))

#将时间元组转换成时间戳
print(time.mktime(time.strptime(timeStr,"%Y-%m-%d %H:%M:%S" )))
