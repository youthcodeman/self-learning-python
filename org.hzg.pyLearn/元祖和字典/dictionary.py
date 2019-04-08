#_*_ coding:utf-8 _*_

dic01 = {"name":"zhangsan","age":18,"address":"浙江省"}
print(dic01)

#查找
print(dic01['name'])

#修改
dic01['name'] = "lisi"
print(dic01)

#添加
dic01["sex"] = "男"
dic01["hobby"] = "篮球"
print(dic01)

# 清空
dic01.clear()
print(dic01)

dic01 = {"name":"zhangsan","age":18,"address":"浙江省"}
dic01 = str(dic01)
print(type(dic01))

dic02 = {"name":"zhangsan","age":18,"address":"浙江省"}
print(dic02.get('name',"zhangsan"))  # 默认值

if 'name' in dic02 :
    print("包含")
else:
    print("不包含")


print(dic02.keys())
print(dic02.values())

print(dic02.items())

dic03 = {"zhangsan":"beijing","lisi":"shanghai","wangwu":"shenzhen"}
temp = input()
print(dic03.get(temp))

