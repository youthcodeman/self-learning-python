#_*_ coding:utf-8 _*_

# n = 100;
# result = 0;
# while n >= 0:
#     result += n
#     n -= 1
# print(result)
#
#
# a = 1
# while a < 5:
#     print("*" * a)
#     a+=1
#
# print("===========================================================")
#
# lin = 1
# while  lin < 5:
#     count = 0
#     while count < lin:
#         print("*",end = "")
#         count += 1;
#     lin +=1
#     print(" ")
#
# print("====================================")
#
# temp = 25
# while temp > 15:
#     print("成立")
#     temp -=1
# else:
#     print("减到15以下了，不成立了")
#
# temp1 = 5
# while  temp1 >= 0:
#     if temp1 == 3:
#         break
#     print("正常输出")
#     temp1 -= 1

print("===============================")

temp2 = 5
while  temp2 >= 0:
    if temp2 == 3:
        temp2 -= 1
        continue
    print("正常输出 %d" %temp2)
    temp2 -= 1