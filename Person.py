class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age
    @property
    def age(self):
        print("Retrieving {}s age...".format(self.name))
        return self.__age
    @age.setter
    def age(self, value):
        if type(value) is not int:
            print("Age must be a number")
        if value < 0:
            print("Age can’t be negative")
        print("Setting {}s to {}...".format(self.name, value))
        self.__age = age