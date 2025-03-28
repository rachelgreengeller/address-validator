class Student:
    #default constructor
    def __init__(self):
        pass

    college_name="UEM kolkata"
    name="anonymous" #class attr


     #parameterised constructor
    name="anisha"
    def __init__(self, name,marks):
        self.name=name   #instance attributes   #obj attr > class attr
        self.marks=marks
        print("adding new student in database..")
    '''def welcome():
        print("Welcome student",self.name
              )'''

s1=Student("anisha",100)
s1.welcome()
print(s1.name, s1.marks )

s2=Student("laila",89)
print(s2.name, s2.marks)




'''class Car:
    color="blue"
    brand="mercedes"
car1=Car()
print(car1.color)
print(car1.brand)'''
