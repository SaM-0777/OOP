import numpy as np

class Point:

    def __init__(self, x = 2.0, y = 3.0):
        self.x = x
        self.y = y
    
    def distance_to_origin(self):
        return np.sqrt(self.x ** 2 + self.y ** 2)

if __name__ == "__main__":
    obj = Point()
    print(obj.distance_to_origin())