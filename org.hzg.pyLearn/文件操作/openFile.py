#_*_ coding:utf-8 _*_

'''
open(文件名，打开方式)
r：只读
w：只写
a：追加

r+：读写，将文件指针调到文件头部
w+：读写，文件不存在直接创建，文件存在则覆盖源文件
a+：追加读写，将文件指针调到文件末尾
'''

# file1 = open("file1.txt","r",encoding='utf-8')
# print(file1)
# #content = file1.read(5)
# content = file1.readline()
# print(content)
#
# file1.close()

'''
不用手动关闭，可以直接自动关闭
'''
# with open("file1.txt","r",encoding='utf-8') as file1:
#     content = file1.readlines()
#     print(content)

'''
逐行读取文件内容
'''
# file1 = open("file1.txt","r",encoding='utf-8')
# i = 1
# for line in file1:
#     print("第%d行内容是: %s"%(i,line))
#     i += 1
#
# file1.close()

with open("file1.txt","r",encoding='utf-8') as file1:
    i = 1
    for line in file1:
        print("第%d行内容是: %s"%(i,line))
        i += 1