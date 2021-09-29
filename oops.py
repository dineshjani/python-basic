class person:
  
    def __init__(self,name):
        self.tricks=[]
        self.name=name

    def print(self):
         print("name is ",self.name)  
    def add_trick(self,trick):
        self.tricks.append(trick)
    def isemployee(self):
        return True 

class employee(person):
    def isemployee(self):
        return False       

p=person("dinesh")
q=person("suresh")
p.add_trick("angular")
p.add_trick("java")
r=employee("naveen")
print(r.print())
print(r.isemployee())
print(p.tricks)
print(q.tricks)


p.print()
q.print()
