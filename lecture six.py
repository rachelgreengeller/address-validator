'''  #WAF to print the length of a list(list is the parameter)
number=["1","2","3","90"]
heroes=["thor","ironman","captain america","shaktiman"]
def print_len(list):
    print(len(list))

print_len(number)
print_len(heroes)'''

'''#waf to print the elements of a list in a single line(list is the parameter)
number=["1","2","3","4"]
heroes=["thor","ironman","captain america","shaktiman"]
def print_len(list):
    print(len(list))
def print_list(list):
    for item in list:
        print(item, end=" ")

print_list(heroes)
print()'''

'''#WAF in python to find the factorail of n(n is the parameter)
def factorial(n):
    fact=1
    for i in range(1, n+1):
        fact*=i
    print(fact)
factorial(6)'''

'''#WAF in python to convert USD to INR
def convert(usd):
    inr=usd*83
    print("USD=",usd,"INR=", inr)

convert(2)'''

'''#recursive function
def show(n):
    if(n==-1):
        return
    print(n)
    show(n-1)
show(7)'''

'''def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*fact(n-1)
print(fact(6))'''

'''#write a recursive function to calculate the sum of first n natural numbers
def sum(n):
    if(n==0):
        return 0
    return sum(n-1)+n
a=sum(5)
print(a)'''

#write a recursive function to print all elements in a list(hint: use list and index as parameters)
def print_list(list, idx=0):
    if (idx==len(list)):
        return
    print(list[idx])
    print_list(list,idx+1)

fruits=["mango","litchi","apple","banana"]
print_list(fruits)


