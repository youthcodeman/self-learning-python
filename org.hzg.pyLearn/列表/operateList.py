#_*_ coding:utf-8 _*_
list01 = ['zhangsan','lisi','wangwu']
print(list01[2])

list02 = ['zhangsan',['lisi','xiaoqi'],'wangwu']
print(list02[1][1])

#修改
list02[1][1] = 'xiaosan'
print(list02)

#追加 最后
list02.append("ksjahfkjashf")
print(list02)

#追加  指定位置插入
list02.insert(1,"插入到第二个")
print(list02)

#删除元素 pop 默认删除最后一个元素,返回你删除的元素
list03 = ['zhangsan','lisi','wangwu']
temp = list03.pop()
print(temp)
print(list03)
# 删除元素 del 可以指定位置删除
list03 = ['zhangsan','lisi','wangwu']
del(list03[1])  #如果不指定位置，则直接从内存中删除列表
print(list03)

# remove当不知道元素的下标的值时，直接传入元素的值即可
list04 = ['zhangsan','lisi','wangwu']
list04.remove("lisi")
print(list04)


# in
list05 = ['zhangsan','lisi','wangwu']
print("lisi" in list05)

# not in
print("lisi" not in list05)
