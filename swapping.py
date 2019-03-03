a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
print("Before swapping: ",a,b)

a = a + b
b = a - b
a = a - b

#print("After Swapping",a,b)

#print(f"After Swapping {a} {b}")

#print("After Swapping {} {}".format(a,b))

#print(f'First number is {a} Second Number is {b} After swapping:{a} {b} ')

#a , b = b, a

print('First number is {1} Second Number is {0} After swapping:{1} {0}'.format(b,a))
