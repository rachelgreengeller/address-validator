class Person:
    __name= "anonymous"

    def __hello(self):
        print("hello person")
    
    def welcome(self):
        self.__hello()
p1=Person()

print(p1.welcome())
#it is done to prevent instance attributes of the class