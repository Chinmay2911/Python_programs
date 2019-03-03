def main():
	menu = int (input('Select any option: \n1. Area of circle \n2. Area of Square \n3. Area of rectangle\n'))
	if menu==1:
		areaofcircle()
	elif menu == 2:
		areaofsquare()
	elif menu == 3 :
		areaofrectangle()
	else :
		print('Enter a valid input.')
	
def areaofcircle():
	PI = 3.14159265359
	radius = int(input("Enter the radius of the circle :"))

	area = PI * radius * radius
	circumference = PI * radius * 2

	print("area of the circle with radius {} is {}" .format(radius,area))
	print(f"circumference of the circle with radius {radius} is {circumference}")
	
def areaofsquare():
	length = int(input("Enter side of the square :"))


	area = length * length
	perimeter = 2 * (length + length)

	print("area of the square with side {} is {}" .format(length,area))
	print("perimeter of the square with side {} is {}" .format(length,perimeter))
	
def areaofrectangle():
	length = int(input("Enter length of the rectangle :"))
	breadth = int(input("Enter breadth of the rectangle :"))

	area = length * breadth
	perimeter = 2 * (length + breadth)

	print("area of the rectangle with length {} and breadth {} is {}" .format(length,breadth,area))
	print("perimeter of the rectangle with length {} and breadth {} is {}" .format(length,breadth,perimeter))

if __name__=='__main__' : main()