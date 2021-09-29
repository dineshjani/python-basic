def Func(s1):
    return s1[0]
fruits = ['Mango','Watermelon', 'Banana', 'Kiwi'] 
print("The list of fruits are as follows:",fruits)
fruits.sort(reverse=True, key=Func)
print("The list of fruits will be sorted according to the length of the letters in descending order:")
print(fruits)

class Student:
    def __init__(self,name,rollno,grade):
        self.name=name
        self.rollno=rollno
        self.grade=grade
    def __repr__(self):
        return f"{self.name}-{self.rollno}-{self.grade}"
        


#Initializing Student Objects
s1=Student("karthi",15,"second")
s2=Student("Indhu",12,"fifth")
s3=Student("Sarvesh",21,"first")


#Creating list of student objects
s4=[s1,s2,s3]

#Sorting list of objects
#Defining lambda function which will return rollno of the object

s5=sorted(s4,key=lambda x:x.rollno) 
print (s5)   