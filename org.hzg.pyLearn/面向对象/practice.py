#_*_ coding:utf-8 _*_

class hero() :
    '''
        英雄类
    '''
    def __init__(self,name,category,output,skill):
        self.name = name
        self.category = category
        self.output = output
        self.skill = skill

    def stoleRedBuff(self):
        print("%s释放了%s技能，偷到红buff，消耗了300血量"%(self.name,self.skill))
        tempOutput = self.output - 300
        if tempOutput < 0:
            print("%s几经阵亡"%self.name)
        else:
            print("%s当前血量还剩%d"%(self.name,tempOutput))

    def soloFight(self):
        print("%s拿到了一血，消耗了500血量" % (self.name))
        tempOutput = self.output - 500
        if tempOutput < 0:
            print("%s几经阵亡" % self.name)
        else:
            print("%s当前血量还剩%d" % (self.name, tempOutput))

    def addOutput(self):
        print("%s加血，补充了200血量" % (self.name))
        tempOutput = self.output + 200
        print("%s当前血量还剩%d" % (self.name, tempOutput))


kai = hero("铠","战士",1000,"急刃风暴")
wangzhaojun = hero("王昭君","法师",1000,"凛冬将至")
ake = hero("阿珂","刺客",1000,"瞬华")

kai.stoleRedBuff()
wangzhaojun.soloFight()
ake.soloFight()

ake.addOutput()