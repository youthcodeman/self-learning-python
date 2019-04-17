#_*_ coding:utf-8 _*_
class Parent1():
    def __init__(self,para1):
        self.para1 = para1

    def a(self):
        print("Parent1中的a方法，参数：" + self.para1)


class Parent2():
    def __init__(self,para2):
        self.para2 = para2

    def a(self):
        print("Parent2中的a方法，参数：" + self.para2)

class Parent3():
    def __init__(self,para3):
        self.para3 = para3

    def a(self):
        print("Parent3中的a方法，参数：" + self.para3)


class Child(Parent1,Parent2,Parent3) :
    def __init__(self,para1,para2,para3):
        # super(Parent1, self).__init__(para1)
        # super(Parent2, self).__init__(para2)
        # super(Parent3, self).__init__(para3)
        Parent1.__init__(self, para1)
        Parent2.__init__(self, para2)
        Parent3.__init__(self, para3)


child01 = Child("1","2","3")
child01.a()