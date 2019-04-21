#_*_ coding:utf-8 _*_
'''
直接覆盖掉原来的内容
'''
# file1 = open("file1.txt","w",encoding="utf-8")
# file1.write("hello world")
#
# file1.close()

'''
追加的方式
'''
# file1 = open("file1.txt","a",encoding="utf-8")
# file1.write("this is append")
#
# file1.close()

'''
tell 查看文件指针
'''
# file1 = open("file1.txt","r",encoding="utf-8")
# print(file1.read(5))
# print(file1.tell())
# print(file1.read(10))
# print(file1.tell())
# file1.close()

'''
seek 设置指针
'''
# file1 = open("file1.txt","r",encoding="utf-8")
# file1.seek(0,5) #第一个参数表示设置指针位置，第二个参数表示偏移量
# print(file1.read())
# file1.close()


i = 1
file1 = open("guest.txt","a",encoding="utf-8")
while True:
    if i < 5:
        name = input("请输入您的姓名")
        file1.write(name + "/n")
        file1.flush()
        i += 1
    else:
        file1.close()
        break

