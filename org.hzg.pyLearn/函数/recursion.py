#_*_ coding:utf-8 _*_

'''
利用递归计算5的阶乘
'''
result = 1

def facte(n) :
    if n == 1:
        return 1
    else :
        return n * facte(n-1)

print(facte(666))