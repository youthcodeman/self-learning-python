#_*_ coding:utf-8 _*_

import numpy as np

arr1 = np.array([1,2,3])
print(arr1)

arr2 = np.array((2,3,4,5,6,6,7,8))
print(arr2)

arr3 = np.array([
    [1,2,4,5,6],
    [1,2,4,5,6],
    [1,2,4,5,6]
])

print(arr3)

#创建一个全0数组
arr4 = np.zeros((50,50),dtype=int)
print(arr4)

arr5 = np.zeros((3,3,3),dtype=str)
print(arr5)

#创建一个全1数组
arr6 = np.ones((3,3,3),dtype=int)
print(arr6)

#其他创建方式
arr7 = np.arange(0,20,1,dtype=int)
print(arr7)

arr8 = np.arange(20,0,-1,dtype=float)
print(arr8)

arr9 = np.linspace(0,20,5) # 等差数列 开始   结束    元素个数
print(arr9)

arr10 = np.logspace(0,2,5) # 等比数列  10的0次方开始 10的2结束  产生5个
print(arr10)

arr11 = np.logspace(1,3,4,base=2)  # 修改底数
print(arr11)

arr12 = np.random.rand(3,3)
print(arr12)

arr13 = np.random.randint(0,5,size=50)
print(arr13)

arr14 = np.random.randn(3,3)  #生成一个正态分布的数组
print(arr14)