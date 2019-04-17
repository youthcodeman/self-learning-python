#_*_ coding:utf-8 _*_

class Animal() :
    def __init__(self,name,food):
        self.name = name
        self.food = food

    def eat(self):
        print("%s爱吃%s"%(self.name,self.food))

class Dog(Animal) :
    def __init__(self,name,food,drink):
        #Animal.__init__(self,name,food)
        super(Dog, self).__init__(name,food)
        self.drink = drink

    def drinks(self):
        print("%s爱喝%s"%(self.name,self.drink))

dog01 = Dog("狼狗","肉","水")
dog01.eat()
dog01.drinks()