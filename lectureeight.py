class Student:   #lets practise question check in ipad
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    
    def get_avg(self):
        sum=0
        for val in self.marks:
            sum+=val
        print("hi", self.name," your avg score is :", sum/3)



s1=Student("anisha biswas",[99,98,97])
print(s1.name, s1.marks)
s1.get_avg()


