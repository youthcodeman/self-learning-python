#_*_ coding:utf-8 _*_
# list01 = [1,2,3,4,5,6,7,8,9,10]
# for i in list01:
#     print(i)

# tup01 = (1,2,3,4,5,6,7,8,9)
# for j in tup01:
#     print(j)

# list02 = [[1,2,1],[5,6,7,8],[9,7,65,4,4],[3,4,5,6,7,8]]
# for m in list02:
#     if type(m) == list:
#         for n in m:
#             print(n,end=" ")
#         print()


dic = {"num01":[1,2,3,4,5],"num02":[6,7,8,9,10]}
for tempDic in dic:
    tmp = dic.get(tempDic)
    print(tempDic)
    if type(tmp) == list:
        for ttmp in tmp:
            print(ttmp,end=" ")

        print()