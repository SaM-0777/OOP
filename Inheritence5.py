class Polygon(object):
    
    def __init__(self, sides):
        self.sides = sides
        self.side_length = [0 for i in range(sides)]
    
    def Input(self):
        self.side_length = [float(input("Side " + str(i + 1) + ": ")) for i in range(self.sides)]

    def Perimeter(self):
        P = 0
        for i in range(self.sides):
            P += self.side_length[i]
        print("Perimeter of Polygon : ", P)

class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self, 3)
    
    def Area(self):
        a, b, c = self.side_length
        S = (a + b + c) / 2
        Area = (S * (S - a) * (S - b) * (S - c)) ** 0.5
        print("Area of Triangle : ", Area)

T = Triangle()
T.Input()
T.Perimeter()
T.Area()
