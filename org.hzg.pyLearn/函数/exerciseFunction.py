#_*_ coding:utf-8 _*_

'''
计算传入字符串的长度
'''
# def countStrLen(str1) :
#     if isinstance(str1,str):
#         print(len(str1))
#     else :
#         print("类型错误")
#
# countStrLen(input())

'''
判断用户传入字符串，列表，元组，字典长度是否大于三
'''
# def ifDataLengthMoreThanThree(data) :
#     if isinstance(data,str) :
#         if len(data) > 3:
#             print("字符串大于三")
#         else :
#             print("字符串小于三")
#     elif isinstance(data,list):
#         if len(data) > 3:
#             print("列表大于三")
#         else :
#             print("列表小于三")
#     elif isinstance(data,tuple):
#         if len(data) > 3:
#             print("元组大于三")
#         else :
#             print("元组小于三")
#     elif isinstance(data, dict):
#         if len(data) > 3:
#             print("字典大于三")
#         else:
#             print("字典小于三")
#
#
# #ifDataLengthMoreThanThree("jk")
# # ifDataLengthMoreThanThree([1,2])
# # ifDataLengthMoreThanThree(([1,2],[3,4],[5,8],[1]))
# ifDataLengthMoreThanThree({"name":"zhangsan","sex":"男","birth":"19941002"})

'''
写入不定个数的字符串，拼接第一个和最后一个字符串
'''
# def combineFirstAndLastStr(data) :
#     if len(data) <= 1 :
#         return "输入类型不准确"
#     first = data[0]
#     last = data[len(data) - 1]
#     print(first + last)
#
# combineFirstAndLastStr(["woaini","bukeneng","zaiyiqi","zhr"])

# def combineFirstAndLastStr1(*args) :
#     print(args[0] + args[-1])
# combineFirstAndLastStr1("woaini","10","zhr")

'''
传入多个参数，以list形式返回
'''
# def createReturnList(*args) :
#     list01 = [];
#     for i in args:
#         list01.append(i)
#
#     return list01
# print(createReturnList("wo","ai","ni","zh","r"))

'''
定义一个函数，返回所有入参的和
'''
# def getSum(*args) :
#     result = 0
#     for i in args:
#         if  isinstance(i,int) :
#             result += i
#
#     return result
#
# print(getSum(1,2,3,4,5,"nimabi"))

'''
输入一个数，根据其是奇数还是偶数分别算出该数的奇数积和偶数积
'''
def evenSum(n) :
    result = 0
    for i in range(2,n + 2,2):
        result += 1/n

    return result

def unEvenSum(n) :
    result = 0
    for i in range(1,n + 2,2):
        result += 1/n
    return result

def main():
    result = 0
    num = int(input())
    if num % 2 == 0:
        result = evenSum(num)
    else :
        result = unEvenSum(num)
    print(result)

main()







