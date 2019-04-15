#_*_ coding:utf-8 _*_
# a = lambda : "xxxx"
# print(a())

# s =  lambda a : a * 50
# print(s("i love you "))

# m = lambda a,b : a*b
# print(m(2000000,5000000))

# m = lambda a,b : a if a > b else b
# print(m(5,4))

# dic = {"a":1,"c":3,"b":2}
# #dic = sorted(dic)  #只是将字典中的key进行排序，并且返回排序后的key的列表
# dic = sorted(dic.items(),reverse=True)
# print({k:v for k,v in dic})

# dic = {"a":1,"c":3,"b":2}
# dic = sorted(dic.items(),key= lambda x:x[1],reverse=True) #字典需要转换成元组列表进行排序
# print({k:v for k,v in dic})

list01 = [
    {"name":"zhangsan","age":18},
    {"name":"lisi","age":20},
    {"name":"wangwu","age":19}
]
dic = sorted(list01,key=lambda x:x['age'],reverse=True)
print(dic)