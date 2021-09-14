class Car:
    __maxspeed = 0
    __name = ""
    def __init__(self):
        self.__maxspeed = "OOP Course"
        self.__name = "Supercar"

    def drive(self):
        print("driving, maxspeed " + str(self.__maxspeed), str(self.__name))

redcar = Car()
redcar.drive()