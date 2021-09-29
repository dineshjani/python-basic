class Computer:
    wheel=4

    def __init__(self,m,n):
        self.first=m
        self.second=n
        print("using constructor",m,n)
    def __add__(self,other):
        m1=self.first+other.first
        m2=self.second+other.second
        return Computer(m1,m2)
    def print(self):
        print(self.first,self.second)

    def config (self):
        print(self.wheel)
        self.wheel=6
        print("config method")
    @classmethod
    def classmethod(cls):
        print("calling class method")
    @staticmethod
    def add3(number):
        return number+3

class SubCompter(Computer):
    def __init__(self):
        super().__init__(2,3)
        print("constructor of child")


subcom1=SubCompter()
print(subcom1.add3(4))
com1=Computer(2,3)
com2=Computer(3,4)
com3=com1+com2
com3.print()
print(Computer.add3(3))
print(com1.add3(3))

Computer.config(com1)
Computer.classmethod()
print(com2.wheel)
print(id(com1))
print(id(com2))