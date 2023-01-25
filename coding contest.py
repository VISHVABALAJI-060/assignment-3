

str=input("Enter the charecter : ")
key=int(input("Enter the key value : "))
for i in str:
    x=ord(i)
    x=x+key
    y=chr(x)
    print(y,end="")
