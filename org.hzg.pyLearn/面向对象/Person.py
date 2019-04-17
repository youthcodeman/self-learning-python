#_*_ coding:utf-8 _*_

class Person() :
    '''
        person类
    '''

    country = "中国"

    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex

    def getPersonInfo(self):
        print("姓名：%s"%self.name)
        print("性别：%s"%self.sex)
        print("年龄：%d"%self.age)
        print("我来自%s"%Person.country)


person01 = Person("zhangsan",18,"男")
person01.getPersonInfo()
print("============================")
print(getattr(person01,"name"))
print(hasattr(person01,"name"))
setattr(person01,"name","lisi")
print(getattr(person01,"name"))
delattr(person01,"name")
#print(getattr(person01,"name"))
print(Person.country)              #类属性
print("===========================")

'''
内置内属性
'''
print(person01.__dict__)
print(person01.__doc__)
print(Person.__name__)
print(Person.__bases__)
