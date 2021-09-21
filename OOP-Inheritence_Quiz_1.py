## Problem 1
class Player(object):
    Max_Pos = 10.0
    def __init__(self):
        self.Pos = 0.0
print("Max Position : ", Player.Max_Pos)    # 10.0
P1 = Player()
P2 = Player()
print("P1 - MaxSpeed : ", P1.Max_Pos)   # 10.0
print("P2 - MaxSpeed : ", P2.Max_Pos)   # 10.0
P1.Max_Pos = 50.0
print("P1 - MaxSpeed : ", P1.Max_Pos)   # 50.0
print("P2 - MaxSpeed : ", P2.Max_Pos)   # 10.0

class Racer(Player):
    Max_Speed = 60.0

P = Player()
R = Racer()

#print("P.Max_Speed : ", P.Max_Speed)    # Error Parent class cannot access class attributes of child Class
print("R.Max_Speed : ", R.Max_Speed)
print("P.Max_Pos : ", P.Max_Pos)
print("R.Max_Pos : ", R.Max_Pos)

## Problem 2
class Employee(object):
    def __init__(self, name, salary = 30000):
        self.Name = name
        self.salary = salary
    
    def Raise(self, amount):
        self.salary += amount

class Manager(Employee):
    def Display(self):
        print("Manager : ", self.name)
    
    def __init__(self, name, salary = 50000, project = None):
        Employee.__init__(self, name, salary)
        self.Project = project
    
    def Bonus(self, amount, bonus = 1.25):
        new_amount = amount * bonus
        Employee.Raise(self, new_amount)
    
M = Manager("Ram", 78500)
M.Raise(1000)
print(M.salary)
M.Bonus(1000, 1.03)
print(M.salary)

# Problem 3
## @classmethod Decorator
class MyDate(object):
    def __init__(self, year, month, day):
        self.year, self.month, self.day = year, month, day

    @classmethod
    def From_str(cls, Datestr):
        Dates = Datestr.split("-")
        day, month, year = int(Dates[0]), int(Dates[1]), int(Dates[2])
        return cls(day, month, year)

D = MyDate.From_str("29-02-2021")
print(D.day, D.month, D.year)

# Problem 4
class Employee(object):
    Min_Salary = 30000
    def __init__(self, Name, salary = Min_Salary):
        self.Name = Name
        if salary >= Employee.Min_Salary:
            self.Salary = salary
    
    def Raise(self, amnt):
        self.Salary += amnt

class Manager(Employee):
    def __init__(self, Name):
        self.Name = Name
        Employee.__init__(self, Name, 50000)

M = Manager("Ram")
print(M.Name)
M.Raise(5000)
print(M.Salary)


# Problem 5
# Intro to abstract method

from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def billpay(self, amount):
        pass

class CreditCardPayemnt(Payment):
    def billpay(self, amount):
        print("Credit Card Payment of : ", amount)

class MobilePayment(Payment):
    def billpay(self, amount):
        print("Mobile Payment of : ", amount)

C = CreditCardPayemnt()
C.billpay(2000.00)

M = MobilePayment()
M.billpay(5000.00)


# Problem 6
class Payment(ABC):
  def Receipt(self, amount):
    print("Purchase of amount : ", amount)
  @abstractmethod
  def payment(self, amount):
    pass

class CreditCardPayment(Payment):
  def payment(self, amount):
    print("Credit card payment of : ", amount)

class MobilePayment(Payment):
  def payment(self, amount):
    print("Mobile wallet payment of : ", amount)

obj = CreditCardPayment()
obj.payment(5000.00)
obj.Receipt(200.00)
print(isinstance(obj, Payment))
obj = MobilePayment()
obj.payment(750.00)
obj.Receipt(4000.00)
print(isinstance(obj, Payment))


# Problem 7
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def Display(self):
    print("In parent class Display method")
    print(self.name)
    print(self.age)

class Employee(Person):
  def __init__(self, name, age, id):
    super().__init__(name, age)
    self.empId = id

  def Display(self):
    print("In child class Display method")
    print(self.name)
    print(self.age)
    print(self.empId)

P = Person("Abhisek", 20)
P.Display()
E = Employee("Abhisek", 20, "CS200")
E.Display()