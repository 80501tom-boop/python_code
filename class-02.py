class A:
    x = []
a1 = A()
a2 = A()
a1.x.append(1)
a2.x.append(2)
print(a1.x)
print(a2.x)

############
class B:
    def __init__(self):
        self.y = []
b1 = B()
b2 = B()
b1.y.append(1)
b2.y.append(2)
print(b1.y)
print(b2.y)