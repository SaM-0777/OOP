class Person(object):
    def __init__(self, name, IDno):
        self.name = name
        self.IDno = IDno
    def Show(self):
        print("Person's Name : ", self.name)
        print("Person's Id : ", self.IDno)

class Student(Person):
    def __init__(self, name, IDno, DeptId, state):
        self.name = name
        self.IDno = IDno
        self.DeptId = DeptId
        self.state = state
        Person.__init__(self, name, IDno)
    def Details(self):
        print("Student's Name : ", self.name)
        print("Student's ID : ", self.IDno)
        print("Student's Dept : ", self.DeptId)
        print("Student's state : ", self.state)

S = Student("Rohan", "20ec14", "ECE", "AP")
S.Show()
S.Details()