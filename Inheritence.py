##single level Inheritence

class Parent:
    def Show(self):
        print("Parent Method")
class child(Parent):
    def show(self):
        print("Child Method")
c = child()
c.show()
c.Show()


##Multilevel Inheritence

class A:
    def MethodA(self):
        print("Class A")
class B(A):
    def MethodB(self):
        print("Class B")
class C(B):
    def MethodC(self):
        print("Class C")
c = C()
c.MethodA()
c.MethodB()
c.MethodC()


##Multiple Inheritence

class A:
    def MethodA(self):
        print("Class A")
class B:
    def MethodB(self):
        print("Class B")
class C(A, B):
    def MethodC(self):
        def MethodC(self):
            print("Class C")
c = C()
c.MethodC()
c.MethodA()
c.MethodB()


##Heirarchical Inheritence

class A:
    def MethodA(self):
        print("Class A")
class B(A):
    def MethodB(self):
        print("Class B")
class C(A):
    def MethodC(self):
        print("Class C")
c = C()
c.MethodC()
c.MethodA()
b = B()
b.MethodB()
b.MethodA()


##Hybrid Inheritence
class A:
    def MethodA(self):
        print("Class A")
class B(A):
    def MethodB(self):
        print("Class B")
class C(A):
    def MethodC(self):
        print("Class C")
class D(B, C):
    def MethodD(self):
        print("Class D")

d = D()
d.MethodA()
d.MethodB()
d.MethodC()
d.MethodD()


##Quiz 2

##P - 1
class Player:
    MAX_Position = 10
    def __init__(self):
        self.position = 0
print(Player.MAX_Position)
P = Player()
print(P.MAX_Position)
print(P.position)

class Racer(Player):
    Max_Speed = 50
P = Player()
r = Racer()
##print("P.MaxSpeed : ", P.MAX_Speed) ##Error
print("r.MaxSpeed : ", r.Max_Speed)
print("P.Max_Position : ", P.MAX_Position)
print("r.Max_position : ", r.MAX_Position)

##P - 2
class Employee:
    def __init__(self, name, salary = 30000):
        self.name = name
        self.salary = salary
    def give_raise(self, amount):
        self.salary += amount
class Manager(Employee):
    def Display(self):
        print("Manager : ", self.name)
    def __init__(self, name, salary = 50000, project = None):
        Employee.__init__(self, name, salary)
        self.project = project
    def give_raise(self, amount, bonus = 1.50):
        new_amount = amount * bonus
        Employee.give_raise(self, new_amount)
m = Manager("Ram", 78500)
m.give_raise(1000)
print(m.salary)
m.give_raise(2000, bonus = 1.03)






##  -:End:-  ##