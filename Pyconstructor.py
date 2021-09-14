## __init__ method in Python

class OOPclass:

    strength = 100
    def __init__(self, data):
        self.strength = data
    
    def show(self):
        print(self.strength)

c = OOPclass(200)
c.show()