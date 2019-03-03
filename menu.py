menu = int (input('Select any option: \n1. Area of circle \n2. Area of Square \n3. Area of rectangle\n'))

if menu == 1 :
	PI = 3.14159265359
	radius = int(input("Enter the radius of the circle :"))

	area = PI * radius * radius
	circumference = PI * radius * 2

	print("area of the circle with radius {} is {}" .format(radius,area))
	print(f"circumference of the circle with radius {radius} is {circumference}")
	
elif menu == 2 :
	length = int(input("Enter side of the square :"))


	area = length * length
	perimeter = 2 * (length + length)

	print("area of the square with side {} is {}" .format(length,area))
	print("perimeter of the square with side {} is {}" .format(length,perimeter))

elif menu == 3 :
	length = int(input("Enter length of the rectangle :"))
	breadth = int(input("Enter breadth of the rectangle :"))

	area = length * breadth
	perimeter = 2 * (length + breadth)

	print("area of the rectangle with length {} and breadth {} is {}" .format(length,breadth,area))
	print("perimeter of the rectangle with length {} and breadth {} is {}" .format(length,breadth,perimeter))

else :
	print('enter a valid input.')