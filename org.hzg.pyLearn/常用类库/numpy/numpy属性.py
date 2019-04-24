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

