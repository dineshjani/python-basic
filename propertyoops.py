class Decorator:
    def __init__(self,name):
        self._fg=name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,name):
        self._name=name

    @name.deleter
    def name(self):
        del self.price


d1=Decorator("ram")

d1.name="sita"
print(d1.name)


        

    