#_*_ coding:utf-8 _*_

# 创建元组

tuple01 = (1,2,3,4,5,6,7,8)
print(tuple01[1])

#tuple01[1] = 20
#print(tuple01)     元组创建之后就不能修改了，在项目中可以用来存放配置信息

# del(tuple01)       #彻底删除
# print(tuple01)
tuple02 = (1,2,3,4,5,6,7,8)
print(tuple02[0:3])

print(len(tuple02))

temp = ['a','b','c']
tempTuple = tuple(temp)
print(tempTuple)

tempList = list(tempTuple)
print(tempList)
