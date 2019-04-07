#_*_ coding:utf-8 _*_

#常用字符串函数
str1 = 'hello world'
print(str1.find('lo'))
print(str1.find('l'))

print(str1.index('l'))
#print(str1.index('aaa'))

str2 = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbbbbbb'
str3 = 'a'
print(str2.count(str3,0,len(str2)))

str4 = 'hello world hello china'
print(str4.replace("hello","HELLO"))
print(str4.split(" "))

print(str4.title())
print(str4.capitalize())
print(str4.center(100))