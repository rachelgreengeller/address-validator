'''class Student:
    def __init__(self,name):
        self.name=name

s1=Student("Anisha")
print(s1.name)'''


#lecture9 check ipad for notes
class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no=acc_no
        self.__acc_pass=acc_pass

    def reset_pass(self):
        print(self.__acc_pass)


acc1=Account("10000","1207")
print(acc1.acc_no)
#print(acc1.acc_pass)
print(acc1.reset_pass())   
