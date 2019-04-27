#_*_ coding:utf-8 _*_

import numpy as np

# 矩阵的秩

arr1 = np.random.rand(3,5)
print(arr1.ndim)   #矩阵的秩
print(arr1.shape)  #矩阵的形状
print(arr1.dtype)   #矩阵的数据类型
print(arr1.size)    #矩阵数据个数

arr2 = arr1.shape = (5,3)
print(arr2)

print("===========================================")

arr3 = np.random.rand(3,5)
print(arr3)
arr3.shape = (5,3)
print(arr3)
arr3.shape = (-1,5)   # 表示设置五列，行数不定
print(arr3)
arr3.shape = (3,-1)   # 表示设置3行，列数不定
print(arr3)

print("=============================================")

arr4 = np.arange(1,10,1,dtype=int)
print(arr4)
arr5 = arr4.reshape(3,3)
print(arr5)
