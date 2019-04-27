#_*_ coding:utf-8 _*_

import numpy as np

# arr1 = np.arange(0,20,1,dtype=int)
# print(arr1)
# print(arr1*6)
# print(arr1 + 5)
#
# arr2 = np.random.rand(3,5)
# print(arr2*50)
#
# #矩阵积
# arr3 = np.array([
#     [1,2,4,5,6],
#     [1,2,4,5,6],
#     [1,2,4,5,6]
# ])
#
# arr4 = np.array([
#     [1,3,5],
#     [1,3,5],
#     [1,3,5],
#     [1,3,5],
#     [1,3,5]
# ])
# print(np.dot(arr3,arr4))  # 3 * 5   5 * 3  = 3 * 3
#
# print("=================================================")
# #矩阵的索引和切片
# arr5 = np.random.randint(1,9,(2,3,3),dtype=int)
# print(arr5)
# print(arr5[0][0][0])
# print(arr5[1][1][2])
#
# print(arr5[:,:,1:])
# print("==================")
# print(arr5[1,:,1:])

#花式索引
arr6 = np.random.randint(1,9,(8,4),dtype=int)
print(arr6)

print(arr6[[0,3,5]])  #获取0,3,5行数据
print(arr6[[0,3,5],[0,3,2]])  #获取 0,0    3,3     5,2 位置的数据
print(arr6[np.ix_([0,3,5],[0,3,2])])  # 利用索引器获取第0 行的0,3,2数据，第3 行的0,3,2数据，第5 行的0,3,2数据


#布尔索引
print("============================")
arr7 = np.arange(1,10,2)
print(arr7 < 10)

print("=============================")
arr8 = np.array([
    [1,2,3],
    [4,5,6]
])
print(arr8[[True,False]])