class Car:    #inheritance check ipad
    #color="black"
    @staticmethod
    def start():
        print("car started...")

    
    @staticmethod
    def stop():
        print("car stopped...")


class ToyotaCar(Car):
    def __init__(self,name):
        self.name=name

car1=ToyotaCar("fortuner")
car2=ToyotaCar("prius")

print(car1.start())
print(car1.name)
#print(car1.color)
print(car2.name)

class Fortuner(ToyotaCar):
    def __init__(self,type):
        self.type=type

car1=Fortuner("diesel")
car1.start()

    