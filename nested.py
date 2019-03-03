'''
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))

if (a>b):
    if(a>c):
        print(str(a) + " is greatest")
    else:
        print(str(c) + " is greatest")
else:
    if(b>c):
        print(str(b) + " is greatest")
    else:
        print(str(c) + " is greatest")
'''    
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))

if((a>b) and (a>c)):
    print(str(a)+" is greatest")

elif ((b>a) and (b>c)):
    print(str(b)+" is greatest")

else:
    print(str(c)+" is greatest")
