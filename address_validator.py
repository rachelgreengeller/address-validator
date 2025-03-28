def addressVal(address):
    dot=address.find(".")
    at=address.find("@")
    if (dot==1):
        print("Invalid")
    elif(at==-1):
        print("Invalid")
    else:
        print("valid")

print("This program will decide if your input is a validd email address")
while(True):
    print("A valid email address needs a '@' symbol and a '.' symbol")
    x=input("Input your email address: ")

    addressVal(x)
