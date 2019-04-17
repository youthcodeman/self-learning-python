#_*_ coding:utf-8 _*_
'''
map
'''
# list01 = [1,2,3,4,5,6,7,8,9]
# list02 = [1,2,3,4,5,6,7,8,9]
# map = map(lambda x,y : x * y,list01,list02)
# print(list(map))

'''
filter
'''
# list01 = [1,2,3,4,5,6,7,8,9]
# filter = filter(lambda x : x > 5,list01)
# print(list(filter))

'''
reduce
'''
from functools import reduce
list02 = [1,2,3,4,5,6,7,8,9,10]
new_list = reduce(lambda x,y:x + y,list02,0)
print(new_list)