class A(object):
    def __init__(self, N):
        self.N = N
        print("Class A value : ", self.N)

class B(A):
    def __init__(self, R, N):
        self.R = R
        print("Class B value : ", self.R)
        A.__init__(self, N)

b = B(50.0, 32.0)