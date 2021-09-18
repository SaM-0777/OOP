## Super() fn

class A(object):
    x = 100
    def MA(self):
        print("Class A")
class B(A):
    def MB(self):
        print("Class B")
        super().MA()
        print(super().x)

b = B()
b.MB()