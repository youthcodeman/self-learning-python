#_*_ coding:utf-8 _*_

# n = 9
# if n % 2 == 0:
#     print("偶数")
# else :
#     print("奇数")
#
#
#
# m = 20
# if m > 50 :
#     print("比50大")
# elif m > 20:
#     print("比20大")
# else:
#     print("小于等于20")
#
#
# a = int(input("请输入第一个数"))
# b = int(input("请输入第二个数"))
# c = int(input("请输入第三个数"))
#
# if a > b:
#     if c > a:
#         print("最大数为：%d"%c)
#     else:print("最大数为：%d"%a)
# elif a > c:
#     if b > a:
#         print("最大数为：%d"%b)
#     else : print("最大数为：%d"%a)
# elif b > a:
#     if c > b:
#         print("最大数为：%d"%c)
#     else : print("最大数为：%d"%b)
# elif b > c:
#     if a > b:
#         print("最大数为：%d"%a)
#     else : print("最大数为：%d"%b)
# elif c > a:
#     if b > c:
#         print("最大数为：%d"%c)
#     else : print("最大数为：%d"%c)
# elif c > b:
#     if a > c:
#         print("最大数为：%d"%a)
#     else : print("最大数为：%d"%c)


# 猜拳游戏
import random
user = input("请输入石头、剪刀、布")
computer = ["石头","剪刀","布"]
rand = random.randint(0,3)

if user == '石头':
    if computer[rand] == "石头":
        print("电脑出石头，平局")
    elif computer[rand] == "剪刀":
        print("电脑出剪刀，用户胜")
    elif computer[rand] == "布":
        print("电脑出布，电脑胜")
elif  user == '剪刀':
    if computer[rand] == "石头":
        print("电脑出石头，电脑胜")
    elif computer[rand] == "剪刀":
        print("电脑出剪刀，平局")
    elif computer[rand] == "布":
        print("电脑出布，用户胜")
elif user == '布':
    if computer[rand] == "石头":
        print("电脑出石头，用户胜")
    elif computer[rand] == "剪刀":
        print("电脑出剪刀，电脑胜")
    elif computer[rand] == "布":
        print("电脑出布，平局")