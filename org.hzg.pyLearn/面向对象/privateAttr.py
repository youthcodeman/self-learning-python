#_*_ coding:utf-8 _*_

'''
python 用双下划线设置属性为私有的
'''
class aaa() :
    def __init__(self,bbb):
        self.__bbb = bbb

    def printbbb(self):
        print(self.__bbb)

cc =  aaa("55555")
cc.printbbb()

'''
强制访问    对象名._类名__私有属性名
'''
print(cc._aaa__bbb)
