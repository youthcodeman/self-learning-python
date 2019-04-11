#_*_ coding:utf-8 _*_

# def pName() :
#     # 声明函数的功能
#     print("这是一个函数")
#
#
# pName()
#
#
# def pName1(userName) :
#     print("我叫%s"%username)
#
#
# pName1("zhangsan")

# def pname2(num1,num2) :
#     a = num1 + num2
#     print("求和结果：%d"%a)
#
#
# # pname2(25,50)
# pname2(num2=5888,num1=9999)   #关键字参数，在调用的时候添加参数的关键字

# def pname2(num1,num2 = 56) :
#     a = num1 + num2
#     print("求和结果：%d"%a)
#
# # pname2(25,50)
# pname2(8688)   #默认值，在函数声明的时候声明默认值，这样在调用的时候可以不用传该参数

#不定长参数
# def pname2(num1,num2,*args,**args1) :
#     a = num1 + num2
#     print("求和结果：%d"%a)
#     print(args)
#     print(args1)
#
# # pname2(25,50)
# #不定长参数，当用*args则表示接受所有未命名的参数，且是一个元组，用**args则表示接受除了必须参数外的所有已经命名的参数，且是一个字典
# pname2(8688,1,'9876','666','7777','45','2',name="zhangsan",age=19,address="浙江省")

#可变对象和不可变对象，可以类比java的值传递和引用传递，传递不可变对象类似于值传递，相当于参数值复制一遍，对原值不会影响
# def temp(str1) :
#     str1 = "hello world"
#     print(str1)
#
# a = "begin"
# print(a)
# temp(a)
# print(a)

#可变对象，相当于传递对象本身，函数中操作该可变对象，则其在内存中的值真实的会发生改变
# def temp(args):
#     args[0] = 2333;
#     print(args)
#
# a = [1,2,3,4,5,6]
# print(a)
# temp(a)
# print(a)

#返回值
# def max(x,y):
#     if x > y :
#         return x
#     else:
#         return y
#
# print(max(5,8))
#
# def temp(x,y):
#     return x,y
#
# num1 = temp(65,86)
# print(num1)
# num2,num3 = temp(65,86)
# print(num2)
# print(num3)

#yield 迭代器
# def temp(a) :
#     i = 0
#     while i < a:
#         yield i
#         i +=1
#
# b = temp(20)
# for c in b:
#     print(c)

# a = [x for x in range(100000000)]
# print(a)

a = (x for x in range(1000))
print(a)
for i in a:
    print(i)
