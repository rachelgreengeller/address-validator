'''class Car:
    def __init__(self):
        self.acc=False
        self.brk=False
        self.clutch=False
    def start(self):
        self.clutch=True   #abstraction
        self.acc=True
        print("car started")

car1=Car()
car1.start()
'''

class Account:  #lets practise check ipad 
    def __init__(self,bal,acc):
        self.balance=bal
        self.account=acc

    #debit method
    def debit(self,amount):
        self.balance-=amount
        print("Rs. ", amount," was debited")
        print("Total balance = ",self.get_balance())

    def credit(self,amount):
        self.balance+=amount
        print("Rs. ",amount," was credited")
        print("Total balance = ",self.get_balance())

    def get_balance(self):
        return self.balance


acc1=Account(10000,12345)
print(acc1.balance)
print(acc1.account)
acc1.debit(1000)
acc1.credit(500)
acc1.credit(40000)
acc1.debit(10000)
acc1.get_balance()



