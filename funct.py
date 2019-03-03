def main():
	function_vk(45,56,34,1,2,3,4,5,6,one=1,two=2,three=3)
	
def function_vk(a, b, c, *args, **kwargs):
	print(a,b,c,)
	for i in args:
		print(i)
	for k in kwargs:
		print(k,'=', kwargs[k])
		
if __name__ == '__main__' : main()