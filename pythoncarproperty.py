from abc import ABC,abstractmethod
# Create your models here.
class Vehicle(ABC):
    @abstractmethod
    def display(self):
        pass


class Car(Vehicle):
    def __init__(self,fuel,name,discount):
        self.fuel=fuel
        self.name=name
        self.discount=discount
    def display(self):
        pass
        
   

class Carmodel(Car):
    def __init__(self,make,model,new_feature,rate, fuel, name, discount):
        super().__init__(fuel, name, discount)
        self.make=make
        self.model=model
        self.new_feature=new_feature
        self.rate=rate

    @property
    def price(self,value):
        return self.price

    @price.setter
    def price(self,value):
        self.price=value-(value*self.discount)/100


    def milegae():
        pass
        
    def get_cost():                      #before save discard discount on that company car
        pass    

print("hello")
d=Carmodel(2007,"s1","x",200,"y","x",10)
from abc import ABC,abstractmethod
# Create your models here.
class Vehicle(ABC):
    @abstractmethod
    def display(self):
        pass


class Car(Vehicle):
    def __init__(self,fuel,name,discount):
        self.fuel=fuel
        self.name=name
        self.discount=discount
    def display(self):
        pass
        
   

class Carmodel(Car):
    def __init__(self,make,model,new_feature,rate, fuel, name, discount):
        super().__init__(fuel, name, discount)
        self.make=make
        self.model=model
        self.new_feature=new_feature
        self.rate=rate

    @property
    def price(self):
        return self.price

    @price.setter
    def price(self,value):
        self.price=value-(value*self.discount)/100


    def milegae():
        pass
        
    def get_cost():                      #before save discard discount on that company car
        pass    

print("hello")
d=Carmodel(2007,"s1","x",200,"y","x",10)
d.price=1000
print(d.price)