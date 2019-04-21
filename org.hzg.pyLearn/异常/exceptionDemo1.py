#_*_ coding:utf-8 _*_

# try:
#     print(aaa)
# except NameError:
#     print("变量未定义")

# try:
#     print(aaa)
# except NameError as e:
#     print(e)
#     print("数值异常")
# finally:
#     print("无论如何都会执行")

# try:
#     #print(aaa)
#     open("aaa.txt","r",encoding="utf-8")
# except (NameError,FileNotFoundError) as e:
#     print(e)
#     print("数值异常")
# finally:
#     print("无论如何都会执行")

try:
    print(aaa)
    open("aaa.txt","r",encoding="utf-8")
except Exception as e:
    print(e)
    print("数值异常")
finally:
    print("无论如何都会执行")