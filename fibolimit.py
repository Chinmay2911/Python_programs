import sys

def fibonacci(n): #generator function
	a, b = 0, 1
	print(a,end = ' ')
	while(b < n):
		yield b
		a, b = b, a + b
      

def main():
	f = fibonacci(200) #f is iterator object

	while True:
		try:
			print (next(f), end=" ")
		except StopIteration:
			sys.exit()
	  
	 
if __name__=='__main__':main()