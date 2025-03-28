'''class Person: 
    name="anonymous"

    def changeName(self,name):
        self.name=name

p1=Person()
p1.changeName("Anisha Biswas")
print(p1.name)
print(Person.name)'''


#we use @property decorator on any method in the class to use the method as a property

class Student:
    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math
        #self.percentage=str((self.phy+self.chem+self.math)/3)+"%"

    #def calculate_percentage(self):
        #self.percentage=str((self.phy+self.chem+self.math)/3)+"%"
        
    @property
    def percentage(self):
        return str((self.phy+self.chem+self.math)/3)+"%"

stu1=Student(98,99,97)
print(stu1.percentage)


stu1.phy=86.5
print(stu1.percentage)
#stu1.calculate_percentage()
#print(stu1.percentage)


