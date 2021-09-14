##The Main Driver function to execute Program in a control manner

class Dog:
    def __init__(self, legs, color):
        self.legs = legs
        self.color = color
    
    def bark(self):
        bark = "bark" * 2
        return bark

if __name__ == "__main__":
    dog = Dog(4, "brown")
    bark = dog.bark()
    print(bark)

##Another Class

class Employee:
    def set_name(self, new_name):
        self.name = new_name
    
    def set_salary(self, new_salary):
        self.salary = new_salary
    
emp = Employee()
emp.set_name("Sam")
emp.set_salary(50000)