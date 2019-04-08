#_*_ coding:utf-8 _*_
import copy
a = [1,2,3,4]
b = a

print(id(a))
print(id(b))  #获取内存地址

a[0] = 5

print(a)
print(b)    # 引用复制 a和b指向同一块内存

#浅拷贝
num1 = 55
num2 = 66
num3 = 77
list1 = [num1,num2,num3]
list2 = list1.copy()
print(id(list1))
print(id(list2))
print(id(list1[0]))
print(id(list2[0]))

print("=======================================")
#深拷贝
num4 = 55
num5 = 66
num6 = 77
list3 = [num4,num5,num6]
list4 = copy.deepcopy(list3)
print(id(list3))
print(id(list4))
print(id(list3[0]))
print(id(list4[0]))