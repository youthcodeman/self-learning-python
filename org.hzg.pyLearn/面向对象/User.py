#_*_ coding:utf-8 _*_
class User() :
    loginCount = 0

    def __init__(self,firstName,lastName,age,sex,phoneNo):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.sex = sex
        self.phoneNo = phoneNo

    def getUserInfo(self):
        personDic = {}
        personDic["姓名"] = self.lastName + self.firstName
        personDic["年龄"] = self.age
        personDic["性别"] = self.sex
        personDic["电话"] = self.phoneNo
        print(personDic)

    def givePeraonalGreet(self):
        if self.sex == "男":
            print("您好：" + self.lastName + "先生")
        else:
            print("您好：" + self.lastName + "女士")

    def changePhoneNo(self,newPhoneNo):
        if len(newPhoneNo) != 11 :
            print("您输入的新号码有误，请重新输入")
            return
        self.phoneNo = newPhoneNo
        print("恭喜您，电话号码修改成功")


    def loginCountIncrement(self):
        User.loginCount += 1
        return User.loginCount



User01 = User("三","张",18,"男","13256859658")
User02 = User("四","王",19,"女","13289756325")

User01.getUserInfo()
User02.getUserInfo()

print("==================================")

User01.givePeraonalGreet()
User02.givePeraonalGreet()

User01.changePhoneNo("13586957568")
User01.getUserInfo()