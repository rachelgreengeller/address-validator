'''f=open("demo.txt","w+")
#f.write("abc")
print(f.read())
f.write("abc")
f.close()'''

'''with open("demo.txt","r") as f:
    data=f.read()
    print(data)

with open("demo.txt","w") as f :
    f.write("new data")'''

'''import os

os.remove("sample.txt")'''

'''with open("practise.txt","r") as f :
    f.write("Hi everyone\nwe are learning File I/O\n")
    f.write("using Java.\nI like programming in Java.\n")'''

'''with open("practise.txt","r") as f:
    data=f.read()

new_data=data.replace("Java","Python")
print(new_data)


with open("practise.txt","w") as f:
    f.write(new_data)'''



'''def check_for_word():
    word="learning"
    with open("practise.txt","r") as f :
       data=f.read()
       if (data.find(word)!=-1):
          print("Found")
       else:
          print("Not found")

check_for_word()

def check_for_line():
   word="anisha"
   data=True
   line_no=1
   with open ("practise.txt","r") as f:
      while data:
         data=f.readline()
         if (word in data):
            print(line_no)
            return
         line_no+=1
      return -1
print(check_for_line())'''

count=0
with open("practise.txt","r") as f:
    data=f.read()
    print(data)        #individual number-> parse/casting to int 

    nums=data.split(",")
    for val in nums:
        if(int(val)%2==0):
            count+=1
print("There are",count,"even numbers")

''' num=""
    for i in range(len(data)):
        if (data[i]==","):
            print(num)
            num=""
        else:
            num+=data[i] '''




