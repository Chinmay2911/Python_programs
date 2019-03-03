import sys

def fibonacci(n): #generator function
   a, b, counter = 0, 1, 0
   while True:
      if (counter > n): 
         return
      yield a
      a, b = b, a + b
      counter += 1

def main():
	f = fibonacci(100) #f is iterator object

	while True:
		try:
			print (next(f), end=" ")
		except StopIteration:
			sys.exit()
	  
	 
if __name__=='__main__':main()