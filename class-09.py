class Father:
    def __init__(self):
        self.x = 50

    def printInfo(self):
        print(f"父類別方法：x = {self.x}")

class Child(Father):
    def __init__(self):
        super().__init__()   # 呼叫父類別的 __init__，繼承 self.x = 50
        self.y = 100         # 子類別自己的屬性

    def printInfo(self):
        super().printInfo()  # 呼叫父類別的 printInfo
        print(f"子類別方法：y = {self.y}")

C = Child()
C.printInfo()