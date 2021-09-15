class Person(object):
    total = 0
    def __init__(self, Name, Age):
        total = 0
        print("Init called")
        self.Name = Name
        self.Age = Age
        Person.total += 1

    def Display(self):
        print(self.Name)
        print(self.Age)

P = Person("Ram", 40)
P.Display()
P = Person("Sita", 32)
P.Display()
print(Person.total)