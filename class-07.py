class Animal:
    def __init__(self, name):
        self.name = name
    def fly(self):
        print(f'{self.name} is flying.')
class Bird(Animal):
    def __init__(self, name):
        self.name = "red" + name
    def sing(self):
        print(f'{self.name} is singing.')
class Bird2(Animal):
    def mymethod(self):
        print("Hello world")
print("...........1...........")
p1 = Bird("sparrow")
print(p1.name)
p1.fly()
p1.sing()
print("...........2...........")
p2 = Bird2("robin")
print(p2.name)
p2.fly()
p2.mymethod()