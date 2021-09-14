##Default/No Condstructor

class OOP:
    strength = 200

    def GetNum(self):
        print(self.strength)
    
o = OOP()
o.GetNum()

##Constructor is Declared
class OOP:
    strength = 200
    def __init__(self):
        self.strength = 100
    def GetNum(self):
        print(self.strength)
o = OOP()
o.GetNum()

##Parameterized constructor
class OOP:
    def __init__(self, data):
        self.strength = data
    def GetNum(self):
        print(self.strength)
o = OOP(50)
o.GetNum()

##Private Methods
class OOP:
    def __init__(self):
        self.__age = 20
    def __printhi(self):
        print("Private Hi")
    def Hello(self):
        self.__printhi()
        print("Hello")
        print("Age : ", self.__age)
o = OOP()
o.Hello()